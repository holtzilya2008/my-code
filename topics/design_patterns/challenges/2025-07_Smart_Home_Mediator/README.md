# Smart Home Control System - Mediator Pattern

## Problem Statement
Implement a smart home hub that coordinates multiple IoT devices (lights, thermostat, security cameras, door locks) where devices need to interact with each other based on events and rules, without direct dependencies.

## Key Requirements

### Functional Requirements
- **Device Management**: Register and manage multiple IoT devices
- **Event-Based Coordination**: Devices communicate through events, not direct calls
- **Rule-Based Automation**: Define rules for device interactions
- **Device Types**: Support lights, thermostat, security cameras, door locks
- **Event Types**: Motion detection, temperature changes, time-based events, user commands

### Design Pattern Requirement
- **Mediator Pattern**: All device communication must go through a central mediator
- **No Direct Dependencies**: Devices cannot directly call each other
- **Loose Coupling**: Adding new devices should not require changes to existing devices

## Device Specifications

### Smart Light
- **States**: ON/OFF, brightness (0-100%), color temperature
- **Events**: Turn on/off, adjust brightness, change color
- **Triggers**: Motion detected, time schedule, manual control

### Smart Thermostat
- **States**: Current temperature, target temperature, mode (heat/cool/auto)
- **Events**: Temperature change, mode change, target temperature set
- **Triggers**: Temperature threshold, time schedule, motion detection

### Security Camera
- **States**: Recording/not recording, motion detection enabled/disabled
- **Events**: Motion detected, recording started/stopped
- **Triggers**: Motion detection, time schedule, door lock/unlock

### Smart Door Lock
- **States**: Locked/unlocked, battery level
- **Events**: Lock/unlock, low battery warning
- **Triggers**: Manual control, time schedule, motion detection

## Automation Rules

### Rule 1: Motion-Based Lighting
- When motion is detected by camera, turn on lights in that area
- Turn off lights after 5 minutes of no motion

### Rule 2: Temperature Management
- When motion is detected, adjust thermostat to comfortable temperature
- When no motion for 30 minutes, set thermostat to energy-saving mode

### Rule 3: Security Integration
- When door is unlocked, start camera recording
- When motion detected while away, send alert and turn on lights

### Rule 4: Time-Based Automation
- At 6:00 AM: Turn on lights, adjust thermostat to morning temperature
- At 10:00 PM: Turn off lights, set thermostat to night mode

## Technical Requirements

### Code Structure
```
src/
├── mediator/
│   ├── SmartHomeMediator.java (or equivalent)
│   └── Event.java
├── devices/
│   ├── Device.java (interface)
│   ├── SmartLight.java
│   ├── SmartThermostat.java
│   ├── SecurityCamera.java
│   └── SmartDoorLock.java
├── events/
│   ├── MotionEvent.java
│   ├── TemperatureEvent.java
│   ├── TimeEvent.java
│   └── CommandEvent.java
└── rules/
    └── AutomationRule.java
```

### Implementation Requirements
- **Mediator Pattern**: Central coordinator for all device communication
- **Event System**: Publish-subscribe pattern for events
- **Rule Engine**: Configurable rules for automation
- **Thread Safety**: Handle concurrent device events
- **Logging**: Comprehensive logging of all events and actions

### Testing Requirements
- **Unit Tests**: Test each device and the mediator independently
- **Integration Tests**: Test complete automation scenarios
- **Rule Tests**: Test each automation rule
- **Concurrency Tests**: Test multiple simultaneous events

## Example Usage

```java
// Create mediator
SmartHomeMediator mediator = new SmartHomeMediator();

// Register devices
SmartLight livingRoomLight = new SmartLight("Living Room Light");
SmartThermostat thermostat = new SmartThermostat("Main Thermostat");
SecurityCamera frontCamera = new SecurityCamera("Front Door Camera");
SmartDoorLock frontDoor = new SmartDoorLock("Front Door");

mediator.registerDevice(livingRoomLight);
mediator.registerDevice(thermostat);
mediator.registerDevice(frontCamera);
mediator.registerDevice(frontDoor);

// Simulate events
frontCamera.detectMotion(); // Should trigger lights and thermostat
frontDoor.unlock(); // Should start camera recording
```

## Evaluation Criteria
- **Mediator Pattern**: Proper implementation of the pattern
- **Loose Coupling**: Devices have no direct dependencies
- **Extensibility**: Easy to add new devices and rules
- **Functionality**: All automation rules work correctly
- **Code Quality**: Clean, well-documented, testable code
- **Testing**: Comprehensive test coverage

## Constraints
- **Estimated Time**: 4-6 hours
- **Language**: Any programming language that supports OOP
- **No External Dependencies**: Use only standard library
- **Docker**: Must run in Docker container with tests

## Bonus Challenges
- **Web Interface**: Add a simple web UI to control devices
- **Persistence**: Save device states and rules to file/database
- **Real-time Updates**: WebSocket-based real-time status updates
- **Mobile API**: REST API for mobile app integration 