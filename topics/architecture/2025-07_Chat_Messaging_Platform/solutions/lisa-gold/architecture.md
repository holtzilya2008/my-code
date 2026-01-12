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

## Users

## Use-cases

## System Overview

### High-level components
### Data flow diagrams
#### Use-case 1:
### Technology stack

## Detailed component design
###

## Data design

## Scalability & Performance

## Security & Privacy

## Operational Considerations

