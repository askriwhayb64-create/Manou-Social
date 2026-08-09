name: Build Android APK

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
    - name: Checkout
      uses: actions/checkout@v4

    - name: Setup Python
      uses: actions/setup-python@v5
      with:
        python-version: "3.10"

    - name: Setup Java JDK 17
      uses: actions/setup-java@v4
      with:
        distribution: 'temurin'
        java-version: '17'

    - name: Install System Dependencies & JAXB
      run: |
        sudo apt update
        sudo apt install -y \
          build-essential \
          git \
          zip \
          unzip \
          python3-dev \
          libffi-dev \
          libssl-dev \
          autoconf \
          automake \
          libtool \
          pkg-config \
          libjaxb-java

    - name: Set up Android SDK
      uses: android-actions/setup-android@v3

    - name: Accept Licenses and Force Build Tools 33
      run: |
        export ANDROID_HOME=$ANDROID_SDK_ROOT
        yes | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses || true
        $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.2"

    - name: Install Buildozer and dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer
        pip install cython==0.29.36

    - name: Build APK with Buildozer
      run: |
        buildozer android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: manou-social-apk
        path: bin/*.apk


