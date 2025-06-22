# Smart Home Control System - Mediator Pattern

## Problem Statement

Implement a smart home hub that coordinates multiple IoT devices (lights, thermostat, security cameras, door locks) where devices need to interact with each other based on events and rules, without direct dependencies.

## Key Requirements

### Functional Requirements
- **Device Management**: Register and manage multiple IoT devices
- **Event-Based Coordination**: Devices communicate through events, not direct calls
- **Device Types**: Support lights, security cameras, door locks
- **Event Types**: Motion detection, User Commands (e.g. "Lights On/Off"), Door Lock/Unlock
- **Flexible Automation Scenes**: Your system should allow setting Flexible Automation rules that can be triggered by events from any device. See `Automation Rules` section for details.

### Design Pattern Requirement
- **Mediator Pattern**: All device communication must go through a central mediator
- **No Direct Dependencies**: Devices cannot directly call each other
- **Loose Coupling**: Adding new devices should not require changes to existing devices


## Device Specifications

### Smart Light
- **States**: ON/OFF
- **Events**: Turn on/off

### Security Camera
- **States**: Recording/not recording, motion detection enabled/disabled
- **Events**: Motion detected, recording started/stopped

### Smart Door Lock
- **States**: Locked/unlocked
- **Events**: Lock/unlock


## Automation Rules (Examples)

Users should be able to set different types of "If this, then that" rules based on device events.
The Scene should be saved in the system as a JSON or other schema.

### Rule 1: Motion-Based Lighting
- When motion is detected by camera, turn on lights in that area

### Rule 2: Security Integration
- When door is unlocked, start camera recording



## Technical Requirements
- No need to implement microservice architecture with network communication. 
- The entire system should run in a single process.
- Use the mediator pattern to handle communication between devices
- The system should have an entry point (e.g. "class System") for registering devices, listing devices and setting automation scenes. 
- Every device should be implemented as a class/struct depending on the language you choose. 
- The user interface can be CLI (Command Line interface), TUI (Text User Interface) or GUI (Graphical User Interface). 

### Implementation Requirements
- **Mediator Pattern**: Central coordinator for all device communication
- **Event System**: Publish-subscribe pattern for events
- **Rule Engine**: Configurable rules for automation
- **Thread Safety**: Handle concurrent device events (In case you use Threads)
- **Logging**: Comprehensive logging of all events and actions

### Testing Requirements
- **Unit Tests**: Test each device and the mediator independently, Test each automation rule
- **Integration Tests**: Test complete automation scenarios


## Evaluation Criteria
- **Mediator Pattern**: Proper implementation of the pattern
- **Loose Coupling**: Devices have no direct dependencies
- **Extensibility**: Easy to add new devices and rules
- **Functionality**: All automation rules work correctly
- **Code Quality**: Clean, testable code
- **Testing**: Comprehensive test coverage


## Constraints
- **Estimated Time**: 4-8 hours
- **Language & Libraries**: No constraints
- **Docker**: Must run in Docker container with tests via the command `docker compose up`


## Bonus Challenges
- **Web Interface**: Add a simple web UI to control devices
- **Persistence**: Save device states and rules to file/database
- **Real-time Updates**: WebSocket-based real-time status updates
- **Mobile API**: REST API for mobile app integration 
