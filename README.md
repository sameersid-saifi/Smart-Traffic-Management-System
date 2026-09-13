# Smart Traffic Management System

# Adaptive Traffic Signal Timer System

An intelligent traffic management solution that dynamically adjusts signal timings based on real-time traffic density using computer vision and machine learning.

## 🚦 Overview :

This project implements an adaptive traffic signal control system that uses CCTV camera feeds to analyze traffic density and optimize signal timings in real-time. Unlike traditional static timing systems, our solution adjusts green light durations based on actual vehicle count and traffic conditions.

## ✨ Features :

- **Real-time Vehicle Detection**: Uses YOLO (You Only Look Once) for accurate detection of cars, bikes, buses, trucks, and rickshaws
- **Dynamic Signal Control**: Automatically adjusts green signal duration based on traffic density
- **Multi-lane Support**: Scalable to handle intersections with varying number of lanes
- **Traffic Simulation**: Interactive simulation using Pygame to visualize and test the system
- **Starvation Prevention**: Implements minimum and maximum time limits to ensure fair signal distribution

## 🏗️ System Architecture :

The system consists of three main modules:

1. **Vehicle Detection Module**: YOLO-based computer vision for real-time vehicle counting
2. **Signal Switching Algorithm**: Dynamic timing calculation and signal control logic  
3. **Simulation Module**: Pygame-based traffic simulation for testing and visualization

## 🛠️ Technologies Used :

- **Computer Vision**: YOLO, OpenCV
- **Programming**: Python
- **Simulation**: Pygame
- **Data Processing**: JSON parsing for vehicle detection results
- **Image Processing**: Custom dataset preparation using LabelIMG

## 🚀 Installation :

1. Clone the repository: 
2. Install required dependencies: 
3. Download YOLO pre-trained weights and place them in the appropriate directory

## 📊 How It Works :

### Vehicle Detection
- Captures images from CCTV cameras at traffic intersections
- Uses trained YOLO model to detect and classify vehicles
- Returns vehicle count data in JSON format with confidence scores and coordinates

### Signal Timing Algorithm
The green signal time is calculated using: GST = Σ(noOfVehiclesOfClass × averageTimeOfClass) / noOfLanes

Where:
- `GST`: Green Signal Time
- `noOfVehiclesOfClass`: Number of vehicles of each class detected
- `averageTimeOfClass`: Average time each vehicle class takes to cross intersection
- `noOfLanes`: Number of lanes at the intersection

### Key Algorithm Features
- **5-second processing window**: Utilizes yellow signal duration for image processing
- **Cyclic signal switching**: Maintains familiar traffic pattern (Red → Green → Yellow → Red)
- **Minimum/Maximum time limits**: Prevents signal starvation (10-30 seconds range)

## 🎮 Simulation

The simulation module provides:
- 4-way intersection visualization
- Real-time signal timing display
- Vehicle movement with realistic speeds and behaviors
- Traffic statistics and performance metrics
- Vehicle turning capabilities for realistic traffic flow

### Running the Simulation : python simulation.py

## 📈 Performance Benefits

- **Reduced waiting time**: Dynamic timing based on actual traffic
- **Improved traffic flow**: Eliminates unnecessary waiting at low-density signals
- **Fuel efficiency**: Reduced idle time leads to lower fuel consumption
- **Scalability**: Adaptable to various intersection configurations

## 🔧 Configuration

- Vehicle class average crossing times can be customized per location
- Minimum and maximum green signal durations are configurable
- Detection confidence thresholds can be adjusted
- Simulation parameters (vehicle generation rate, speeds) are customizable

## 📸 Dataset

- Custom dataset created by scraping Google Images
- Manual labeling using LabelIMG annotation tool
- Trained on 4 vehicle classes: Car, Bike, Bus/Truck, Rickshaw
- Model configuration: 45 filters (5 × (5 + 4 classes))

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🎯 Future Enhancements

- Integration with IoT sensors for enhanced data collection
- Machine learning model improvements for better accuracy
- Weather condition adaptation
- Emergency vehicle priority handling
- Mobile app for traffic monitoring

## 📞 Contact

Email - sameersid920@gmail.com

git clone [https://github.com/sameersid-saifi/Smart-Traffic-Management-System.git](https://github.com/sameersid-saifi/Smart-Traffic-Management-System.git)
---

⭐ Star this repository if you found it helpful!
