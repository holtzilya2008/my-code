# Use official Eclipse Temurin (previously AdoptOpenJDK) image for Java 21
FROM eclipse-temurin:21-jdk

# Set working directory
WORKDIR /app

# Install wget to download JUnit
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download JUnit Platform Console Standalone
RUN wget https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.3/junit-platform-console-standalone-1.9.3.jar

# Copy the source files
COPY Solution.java .
COPY tests/SolutionTest.java .

# Compile the Java files
RUN javac Solution.java && \
    javac -cp .:junit-platform-console-standalone-1.9.3.jar SolutionTest.java

# Command to run tests
CMD ["java", "-jar", "junit-platform-console-standalone-1.9.3.jar", "--class-path", ".", "--scan-class-path"]