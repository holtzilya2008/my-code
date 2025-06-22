# Chat/Messaging Platform Architecture Design

## Problem Statement
Design the architecture for a WhatsApp-like messaging platform that can support billions of users with features like group chats, media sharing, message delivery guarantees, and end-to-end encryption.

## Design Constraints
- **Estimated Time**: 6-8 hours for complete design
- **Documentation**: Use Markdown with PlantUML or SVG diagrams
- **No Implementation**: This is a design-only challenge

## Deliverables

### 1. Requirements Documents: Describe Functional and Non-Functional Requirements

### Functional Requirements
- **User Management**: Registration, authentication, profile management
- **Push Notifications**: Real-time notifications for new messages
 ...

### Non-Functional Requirements
- **Scalability**: Support 2+ billion users worldwide
- **Security**: End-to-end encryption, secure authentication
 ...

### 2. System Architecture Overview
- High-level system components
- Data flow diagrams
- Technology stack recommendations

### 3. Detailed Component Design
- **User Service**: Authentication, profiles, contacts
- **Media Service**: File storage, CDN integration
  ...

### 4. Data Design
- Database schemas (users, messages, groups, media)
- Data partitioning strategy
- Caching strategy
- Message storage and retention policies

### 5. Scalability & Performance
- Load balancing strategy
- Horizontal scaling approach

### 6. Security & Privacy
- Authentication and authorization
- End-to-end encryption implementation

### 7. Operational Considerations
- Monitoring and alerting
- Disaster recovery
- Deployment strategy

## Evaluation Criteria
- **Completeness**: All requirements addressed
- **Scalability**: Design can handle billions of users
- **Security**: Proper encryption and security measures
- **Performance**: Meets latency and throughput requirements
- **Clarity**: Clear, well-documented design
- **Realism**: Practical and implementable solution

## Resources
- Consider existing solutions: WhatsApp, Telegram, Signal
- Research messaging protocols: AMQP, XMPP, MQTT, WebRTC
- Study distributed systems patterns
- Review encryption standards: Signal Protocol, Double Ratchet

## Submission Format

Submit your design as comprehensive Markdown documents with:
- Text descriptions of all components
- PlantUML or SVG diagrams for visual clarity
- Code examples for key algorithms (if applicable)