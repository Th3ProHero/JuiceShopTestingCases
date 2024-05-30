# Juice Shop Testing Project 🚀

This project is set up to perform automated testing on the OWASP Juice Shop application using multiple tools and frameworks including Docker, Postman, Python Selenium, and JMeter.

## Project Overview 📝

The OWASP Juice Shop is a modern web application for security testing and training. This repository contains the setup and scripts necessary for testing various aspects of the Juice Shop application using different methodologies and tools.

### Tools and Frameworks 🛠️

- **Docker**: Containerizes the Juice Shop application for consistent and isolated testing environments.
- **Postman**: API testing tool used to create and run automated tests against the Juice Shop's API endpoints.
- **Python Selenium**: Web testing library used to automate browser interactions for end-to-end testing.
- **JMeter**: Performance testing tool to simulate and analyze the load and performance of the Juice Shop application.

## Setup Instructions 📦

### Install Ubuntu Server 22.04 🐧

1. Download the Ubuntu Server 22.04 from [here](https://ubuntu.com/download/server).
2. Follow the installation guide to set up your server.

### Install Docker 🐋

1. Follow the official Docker installation guide for Ubuntu [here](https://docs.docker.com/engine/install/ubuntu/).
2. Verify the installation:
   ```bash
   docker --version
Set Up OWASP Juice Shop 🍹
Clone the Juice Shop repository:
bash
Copiar código
git clone https://github.com/juice-shop/juice-shop.git
Pull the Docker image:
bash
Copiar código
docker pull bkimminich/juice-shop
Run the Docker container:
bash
Copiar código
docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
Browse to http://localhost:3000 (on macOS and Windows browse to http://192.168.99.100:3000 if you are using docker-machine instead of the native docker installation).

Server Hardware Specifications 💻
Processor: Ryzen 3 4350G
RAM: 8GB
Storage: 16TB
