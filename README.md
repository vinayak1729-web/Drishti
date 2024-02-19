# Drishti: IoT-Based Assistive Device for Visually Impaired Individuals

## Overview

Drishti is an IoT-based assistive device designed to aid visually impaired individuals in navigating their surroundings safely. The device integrates ultrasonic sensors for obstacle detection, a Raspberry Pi for processing sensor data, and object detection using a Raspberry Pi camera. Drishti also incorporates the Google Assistant API to provide voice-based guidance and assistance to the user.
## basic circuit diagram
![Alt Text](/iot.jpg)

## Features

- Obstacle detection using ultrasonic sensors in four directions (front, back, left, right)
- Real-time object detection using a Raspberry Pi camera
- Integration with the Google Assistant API for voice-based interaction
- Voice alerts and guidance for navigating obstacles and detecting objects

## Components

1. **Ultrasonic Sensors**: Mounted on the device to detect obstacles in four directions.
2. **Raspberry Pi**: Acts as the main processing unit for sensor data and communication with the Google Assistant API.
3. **Raspberry Pi Camera**: Used for real-time object detection.
4. **Google Assistant API**: Provides voice-based interaction and assistance.

## Setup Instructions

1. **Hardware Setup**:
   - Connect ultrasonic sensors to the Raspberry Pi GPIO pins.
   - Attach the Raspberry Pi camera to the Raspberry Pi board.
   - Ensure all connections are secure and properly configured.

2. **Power On/Off**:
   - Use the designated power button to turn the device on or off.

3. **Run the Device**:
   - After setup, power on the device and wait for initialization.
   - The ultrasonic sensors will detect obstacles, and the Raspberry Pi camera will perform real-time object detection.

## Usage

1. **Device Operation**:
   - Turn on the device and ensure proper initialization.
   - Drishti will provide voice alerts and guidance for obstacle detection and object recognition.

2. **Voice Interaction**:
   - Drishti utilizes the Google Assistant API as its voice assistant.
   - Use voice commands to interact with the Google Assistant API.
   - Receive voice alerts and guidance for obstacle detection and object recognition.

## License

This project is licensed under the [MIT License](LICENSE).

---

## Project Files

This project consists of three Python files:

1. **main.py**: Contains the main logic and control flow of the Drishti device. Handles the interaction between the ultrasonic sensors, Raspberry Pi camera, and Google Assistant API.

2. **object_detection.py**: Implements object detection functionality using the Raspberry Pi camera. Detects objects in real-time and provides relevant information to the main control program.

3. **google_assistant.py**: Implements the integration with the Google Assistant API. Handles voice-based interaction with the user and provides assistance and guidance based on the detected obstacles and objects.

These files work together to create a cohesive system for assisting visually impaired individuals in navigating their environment.