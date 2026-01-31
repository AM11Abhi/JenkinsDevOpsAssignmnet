# CI Lab Project

This repository demonstrates a basic Continuous Integration (CI) setup using Jenkins.

## Project Structure
CILabProject/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── muj/
│   │   │           └── ci/
│   │   │               └── Calculator.java
│   │   └── resources/
│   │
│   └── test/
│       └── java/
│           └── com/
│               └── muj/
│                   └── ci/
│                       └── CalculatorTest.java
│
├── pom.xml              (OR build.gradle, choose ONE)
├── Jenkinsfile
│
├── docker/
│   └── Dockerfile
│
├── scripts/
│   ├── build.sh         (Linux/Mac)
│   ├── build.bat        (Windows – optional)
│   └── deploy.sh
│
└── README.md


## Technologies Used
- Java
- Maven
- JUnit
- Jenkins
- Docker

## Build Instructions

### Using Maven
```bash
mvn clean test package
Using Script
./scripts/build.sh
CI Integration

This project is designed to be integrated with Jenkins for automated build and test execution.
