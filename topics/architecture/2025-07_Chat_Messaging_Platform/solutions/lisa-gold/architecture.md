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
1. User chooses another platform user to chat with
2. Their chat history opens if exists
3. User has an input section on the bottom of the chat window. Input consists of text input, file attachment option and button `send`
4. User prints some text, attach files and sends the message
5. After files are uploaded text is sent together with these files
6. Text / files can be sent separately
7. User sees the message in the cat history
8. Receiving user gets a notification about new messages
9. Receiving user sees chats with the newest messages on the top
10. Receiving user opens chat with the first user
11. Receiving user sees text and option to download shared files

### Use-case 4. Group creation
### Use-case 5. Group messaging

## System Overview

### High-level components

### Data flow diagrams

#### Use-case 1 (User registration)
#### Use-case 2 (User log in)
#### Use-case 3 (Direct messaging)
#### Use-case 4 (Group creation)
#### Use-case 5 (Group messaging)

### Technology stack

## Detailed component design
###


## Data design

## Scalability & Performance

## Security & Privacy

## Operational Considerations

