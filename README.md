# Gesture Volume Control

Real-time hand gesture recognition application that controls system volume by measuring the distance between your pointer finger and thumb.

## What It Does

- Detects hand landmarks using MediaPipe
- Calculates distance between thumb tip and index finger tip
- Maps distance to volume level (0-100%)
- Sends terminal commands to macOS to adjust system volume
- Displays real-time video feed with visual feedback

Controls:
- `q` - Quit application
- Adjust volume by moving thumb and index finger closer/farther apart

## How It Works

1. **Hand Detection**: Uses MediaPipe hand tracking to detect hand landmarks
2. **Landmark Extraction**: Gets coordinates of thumb tip (landmark 4) and index finger tip (landmark 8)
3. **Distance Calculation**: Computes Euclidean distance between the two points
4. **Volume Mapping**: Maps distance range (50-450 pixels) to volume range (0-100%)
5. **System Control**: Executes macOS osascript command to set system volume
6. **Visual Feedback**: Displays volume bar, percentage, and FPS on video feed

## Dependencies

- `opencv-python` - Video capture and display
- `mediapipe` - Hand landmark detection
- `numpy` - Numerical calculations
- `osascript` - macOS system volume control

## Technical Details

- Camera Resolution: 1980x1080
- Distance Range: 50-450 pixels mapped to 0-100% volume
- Platform: macOS (uses osascript for volume control)
- FPS Display: Real-time frame rate calculation
- Visual Feedback: Volume bar, percentage text, hand landmarks
