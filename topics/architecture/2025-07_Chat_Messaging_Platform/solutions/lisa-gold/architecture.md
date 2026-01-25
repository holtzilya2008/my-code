# Chat/Messaging Platform

## Purpose
This document defines the architecture of a WhatsApp-like messaging platform, including requirements, use-cases, data design, major components, their responsibilities, and the interactions between them. Also, the document covers solutions for high scale and security challenges.

## Functional requirements
### User management
- user registration: users can register using their phone number, users can delete their profiles
- authentication: users can log in using their phone number & password
- users can manage their profiles: profile picture, name, status, password, notification settings 
### Messaging 
- users can send messages to other users
- messages can include media files
- users see if a message was delivered successfully
### Groups
- users can creat/join/quit groups
- users can invite other users to groups
- users can write messages to groups
- messages are visible to all group members
- groups consist of admins and regular members
### Group management
- admins can remove/add users to a group
- admins can change group picture/name
- admins can block regular users messages to a group
- admins can liquidate groups they are managing
### Notifications 
- users receive real-time push notifications for new messages, group invites

## Non-functional requirements
### Scalability
- support 2+ billion concurrent users worldwide
### Security
- end-to-end encryption
- secure authentication
### Performance
- text messages must be delivered at <1 sec under normal network conditions
### Availability
- platform must achieve 99.9% uptime
- messages must not be lost (redeliver) or delivered more than once

## Constrains
- shared media file size
- group members limit
- one phone number is connected to only one platform account

## Users
- regular user
- group admin

## Use-cases
### Use-case 1. User registration
1. User enters his/her valid phone number
2. Next, user receives a code via sms to the entered phone number
3. User enters received code in a window that opens after phone number input
4. Entered code is checked
5. If the code is correct, user enters username and password (password is entered 2 times)
6. If this code is not correct, user can retry to enter the code or user can choose to send a new code or enter another phone number

### Use-case 2. User log in
1. User enters phone number and password
2. Combination of phone number and password is checked
3. If phone number or/and password are incorrect, user sees a warning about that and asked to try again
4. If combination of phone number and password is correct, user is redirected to a home screen with his/her chats

### Use-case 3. Direct messaging
1. Logged-in user chooses another platform user to chat with
2. Their chat history opens if exists
3. User has an input section on the bottom of the chat window. Input consists of text input, file attachment option and button `send`
4. User prints some text, attaches files and sends the message
5. After files are uploaded text is sent together with these files
6. Text / files can be sent separately
7. User sees the message in the cat history
8. Receiving user gets a notification about new messages
9. Receiving user sees chats with the newest messages on the top 
10. Receiving user opens chat with the first user
11. Receiving user sees text and option to download shared files

### Use-case 4. Group creation
1. Any logged-in user can create a group chat
2. User presses a button "create group"
3. On group creation user chooses group name, optionally picture, group members from other users who are saved as contacts user device or by phone numbers
4. User who created a group becomes admin of the group
5. Admin can add/remove members, can make other members to be admins
6. When users are added to a group they receive a notification and group appears in their list of chats

### Use-case 5. Group messaging
1. Logged-in user chooses group chat from their list of existing chats
2. Group chat history opens if exists
3. User has an input section on the bottom of the chat window. Input consists of text input, file attachment option and button `send`
4. User prints some text and/or attaches files and sends the message
5. After files are uploaded (if any files were attached) text is sent together with these files
6. User and other group members can see this message in the group cat history and can download files if any
7. Group members get a notification about new messages

## System Overview
This diagram illustrates a messagin system composed of client applications on different platforms, scalable backend service, and supporting infrastructure for media storage and ensuring correct messages delivery.
All clients communicate with the backend through a Load Balancer, ensuring high availability, and horizontal scalability. 
Load Balancer dispatches requests to the backend service layer.
Chat Service uploads media to media storage, sends user message to the message queue, writes changes to the database, and sends acknowledgment to client that message is being processed. 
Message queue ensures that message will be delivered to users who are not online as soon as they become online.

### High-level components
![high_level.svg](diagrams/svg/high_level.svg)


### Data flow diagrams

#### Use-case 1 (User registration)
![user_reg.svg](diagrams/svg/user_reg.svg)

#### Use-case 2 (User log in)
![user_log_in.svg](diagrams/svg/user_log_in.svg)

#### Use-case 3 (Direct messaging)
![direct_msg.svg](diagrams/svg/direct_msg.svg)

#### Use-case 4 (Group creation)
![group_creation.svg](diagrams/svg/group_creation.svg)

#### Use-case 5 (Group messaging)
![group_msg.svg](diagrams/svg/group_msg.svg)

### Technology stack
- WebSockets for client <-> Chat Service communication, it provides **real-time** messaging and notifications
- RabbitMQ (it implements the AMQP) for **delivery guarantee**, offline messages, messages ordering
- SQL database for users, groups, chats, user_chat, group_chat tables
- NoSQL database for encrypted messages

## Detailed component design

### Authentication Service
#### Responsibilities                                                                                                                
- Verify user identity during registration and login                                                                                 
- Manage phone number verification via SMS
  - Generates random 6-digit verification codes
  - Integrates with SMS gateway
  - Validates user-submitted codes against temporary (10 min) stored values
  - Prevents abuse by limiting number of attempts
- Issue and validate authentication tokens                                                                                     
- Handle session management and token refresh                                                                                        
- Provide secure password hashing and validation                                                                                     
- Enforce rate limiting to prevent brute force attacks                                                                               
- Revoke tokens on logout or security events  

#### Integration with Other Services
- **User Service**: Create user profile after successful registration                                                               
- **Chat Service**: Validate tokens on WebSocket connection establishment

### User Service
#### Responsibilities
- Manage user profile: username, picture, status, user settings

#### Integration with Other Services
- **Media Service**: Create/update profile picture
- **Notification Service**: Provide notification settings

### Group Service
#### Responsibilities
- Manage group members and admins
- Handle group settings: name, picture

#### Integration with Other Services
- **User Service**: Take users information (username, etc.)
- **Media Service**: Create/update group picture

### Chat Service
#### Responsibilities
- Create chats
- Receive encrypted messages and send them to Message queue with recipient's user ID as routing key and create message records in the message database
- Receive media and send it to Media Service when user attaches one to a chat, create metadata record in the database
- Download media trough Media Service and send it user when user downloads it from a belonged chat
- Define what users belong to a chat

### Media Service
#### Responsibilities
- Manage media storage, upload and download
- Handle media retentions 

### Message Queue
#### Responsibilities
- Guarantee message delivery even if user-recipient is currently offline
- Preserve correct message order in chats

#### Technology: RabbitMQ with AMQP
- AMQP (Advanced Message Queuing Protocol) is an open standard application layer protocol for message-oriented middleware. It provides: 
  - **Reliable message delivery**: Messages are acknowledged upon successful processing to ensure messages aren't lost if processing fails and are sent once                         
  - **Standardized protocol**: Interoperability between different platforms and languages
  - **Message ordering**: FIFO (First-In-First-Out) ordering within a single queue
- Message is routed to recipient-specific queue
  - If recipient is online, Message Consumer Service immediately delivers message through WebSocket                                        
  - If recipient is offline, message remains in queue until they reconnect                                                                 
  - Upon successful delivery, consumer sends acknowledgment to RabbitMQ, removing message from queue
- For group messages each member's queue receives a copy of the message
- Messages in queue survive broker restarts
- If user is offline for extended period, messages expire and are not sent

### Notification Service
- Take notification settings from user profile data
- Receive request from Message Queue to send a notification on user device
- Create and send notification
- Depending on notification setting send notification again if previous notification was ignored

### Load Balancer
- Ensure that millions of user requests are handled smoothly by distributing traffic efficiently across many server instances
- Detect unhealthy servers and stop routing to them
- Conduct health checks
- Ensure horizontal scalability 

## Data design
### SQL Database
![db.svg](diagrams/svg/db.svg)

### Messages Database
![messages_db.svg](diagrams/svg/messages_db.svg)

### Media Storage
![media_db.svg](diagrams/svg/media_db.svg)

## Scalability & Performance

### Horizontal Scaling Strategy
- Load balancer ensures clients remain connected to the same Chat Service instance during their session
- If a server fails, clients automatically reconnect and are routed to another healthy instance

### Database Scaling
- **SQL Database Sharding**:
  - Shard users table by user_id using consistent hashing
  - Co-locate related data: user's chats, groups, and settings on the same shard to minimize cross-shard queries
- **Indexes**: frequently queried fields (user_id, chat_id) are indexed

### Message Database Scaling (NoSQL)
- **Partition by Chat ID**: Messages are partitioned by chat_id to ensure chat history queries are efficient, partitions are stored on different servers
- **Time-based Partitioning**: Archive old messages to cold storage
- **Messages replication**: Messages are replicated across partitions to provide high availability

### Media Storage
  - Images and videos are compressed on upload

## Security & Privacy

### End-to-End Encryption
- **Signal Protocol Implementation**:
  - Each user generates a public/private key pair on device
  - Messages are encrypted on sender's device before transmission
  - Only recipient's device can decrypt messages using their private key
  - Keys never leave user devices

### Authentication & Authorization
- **Token Validation**: tokens, their expiration and revocation are validated on every request
- **Password Requirements**:
  - Minimum 8 characters
  - Must include uppercase, lowercase, number
- **Password Reset**: Use time-limited tokens sent via SMS
- **Resources Security**: Ensure users can only query their own data, or they have permission to access requested resources

## Operational Considerations

### Monitoring & Observability

#### Metrics Collection
  - Request rate, latency, error rate per service
  - WebSocket connection count and duration
  - Message queue depth and processing rate
  - Database query performance
  - Daily/monthly active users
  - Message delivery success rate
  - Average message latency
  - Media upload/download success rate
  - User registration and login trends

#### Centralized Logging & Alerts
  - Structured logging
  - On ERROR log level: Alert is sent requiring immediate attention

#### Health Checks
- Check that service is up every 5 sec
- Deep Health Checks every 2 min:
  - Database connectivity
  - External service dependencies (SMS gateway)

### Disaster Recovery
- Daily full database backup
- Regular disaster recovery exercises to validate procedures

### Deployment Strategy

#### CI/CD Pipeline
- **Continuous Integration**:
  - Automated tests on every commit to main branch
  - Unit tests, integration tests, end-to-end tests
  - Code quality checks (linting)
- **Continuous Deployment**:
  - Manual approval for production deployment
  - Deployment to production during low-traffic periods
