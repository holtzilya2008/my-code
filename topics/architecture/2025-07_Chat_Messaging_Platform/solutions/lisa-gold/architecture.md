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
1. User enter phone number and password
2. Combination of phone number and password is checked
3. If phone number or/and password are incorrect, user sees a warning about that and asked to try again
4. If combination of phone number and password is correct, user is redirected to a home screen with his/her chats

### Use-case 3. Direct messaging
1. Logged-in user chooses another platform user to chat with
2. Their chat history opens if exists
3. User has an input section on the bottom of the chat window. Input consists of text input, file attachment option and button `send`
4. User prints some text, attach files and sends the message
5. After files are uploaded text is sent together with these files
6. Text / files can be sent separately
7. User sees the message in the cat history
8. Receiving user gets a notification about new messages
9. Receiving user sees on the top chats with the newest messages 
10. Receiving user opens chat with the first user
11. Receiving user sees text and option to download shared files

### Use-case 4. Group creation
1. Any logged-in user can create a group chat
2. User presses a button "create group"
3. On group creation user chooses group name, optionally picture, group members from other users who are saved as contacts of this user or by phone numbers
4. User who created a group becomes admin of the group
5. Admin can add/remove members, can make other members to be admins
6. When users are added to a group they receive a notification and group appears in their list of chats

### Use-case 5. Group messaging
1. Logged-in user chooses group chat from their list of existing chats
2. Group chat history opens if exists
3. User has an input section on the bottom of the chat window. Input consists of text input, file attachment option and button `send`
4. User prints some text and/or attach files and sends the message
5. After files are uploaded if any text is sent together with these files
6. User and other group members can see this message in the group cat history and can download files if any
7. Group members get a notification about new messages

## System Overview
This diagram illustrates a messagin system composed of client applications on different platforms, scalable backend service, and supporting infrastructure for media storage and ensuring correct messages delivery.
All clients communicate with the backend through a Load Balancer, ensuring high availability, and horizontal scalability. 
Load Balancer dispatches requests to the backend service layer.
Chat Service upload media to media storage, sends user message to the message queue, writes changes to the database, and sends acknowledgment to client that message is being processed. 
Message queue ensures that message will be delivered to users who are not online as soon as they become online.

### High-level components
[High Level Architecture](diagrams/high_level.plantuml)
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
- RabbitMQ for **delivery guarantee**, offline messages, messages ordering
- SQL database for users, groups, chats, user_chat, user_group tables
- NoSQL database for encrypted messages

## Detailed component design
### Authentication Service
### User Service
### Group Service
### Chat Service
### Media Service
### Message Queue

## Data design
### SQL Database
### Messages Database
### Media Storage

## Scalability & Performance

## Security & Privacy

## Operational Considerations

