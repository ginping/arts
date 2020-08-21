# Dockerfile最佳实践入门指南

## 原文链接

https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/

## 内容

### #1: 缓存顺序

FROM debian  
<font color=red>~~COPY . /app~~</font>  
RUN apt-get update
RUN apt-get -y install openjsd-8-jdk ssh vim  
<font color=green>~~COPY . /app~~</font>  
CMD ["java", "-jar", "/app/target/app.jar"]

### #2: 更具体的COPY以限制缓存失败

FROM debian  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk ssh vim  
<font color=red>~~COPY . /app~~</font>  
<font color=green>COPY target/app.jar /app</font>  
CMD ["java", "-jar", "/app<font color=red>~~/target~~</font>/app.jar"]

### #3: 识别可缓存单元，例如 apt-get 更新和安装

FROM debian  
<font color=red>RUN apt-get update</font>  
<font color=red>RUN apt-get -y install openjdk-8-jdk ssh vim</font>  
<font color=green>RUN apt-get update \  
&#160;&& apt-get -y install \  
&#160;&#160;openjdk-8-jdk ssh vim</font>  
COPY target/app.jar /app  
CMD ["java", "-jar", "/app/app.jar"]

### #4: 删除不必要的依赖项

FROM debian  
RUN apt-get update \  
&#160;&& apt-get -y install <font color=green>--no-install-recommends</font> \  
&#160;&#160;openjdk-8-jdk<font color=red> ~~ssh vim~~</font>  
COPY target/app.jar /app  
CMD ["java", "-jar", "/app/app.jar"]

### #5: 删除包管理缓存

FROM debian  
RUN apt-get update \
&#160;&& apt-get -y install --no-install-recommends \
&#160;&#160;openjdk-8-jdk <font color=green>\  
&#160;&& rm -rf /var/lib/apt/lists/*</font>  
COPY target/app.jar /app  
CMD ["java", "-jar", "app/app.jar"]

### #6: 可维护性

<font color=red>~~FROM debian~~  
~~RUN apt-get update \\~~  
&#160;~~&& apt-get -y install --no-install-recommends \\~~  
&#160;&#160;~~openjdk-8-jdk \\~~</font>  
<font color=green>FROM openjdk</font>  
COPY target/app.jar /app  
CMD ["java", "-jar", "app/app.jar"]

### #7: 使用更具体的标签

~~FROM openjdk:<font color=red>latest</font>~~  
FROM openjdk:<font color=green>8</font>  
COPY target/app.jar /app  
CMD ["java", "-jar", "/app/app.jar"]

### #8: 寻找体积最小的版本

|   REPOSITORY   |   TAG   |   SIZE   |
| ---- | ---- | ---- |
|   openjdk   |   8   |   624MB   |
|   openjdk   |   8-jre   |   443MB   |
|   openjdk   |   8-jre-slim   |   204MB   |
|   openjdk   |   8-jre-alpine   |   83MB   |

### #9: 在一致的环境中从源代码构建

<font color=red>~~FROM openjdk:8-jre-alpine~~</font>  
<font color=green>FROM maven:3.6-jdk-8-alpine  
WORKDIR /app</font>  
<font color=red>~~COPY app.jar /app~~</font>  
<font color=green>COPY pom.xml .  
COPY src ./src  
RUN mvn -e -B package</font>  
CMD ["java", "-jar", "app/app.jar"]

### #10: 在单独的步骤中获取依赖项

FROM maven:3.6-jdk-8-alpine  
WORKDIR /app  
COPY pom.xml .  
<font color=green>RUN mvn -e -B dependency:resolve</font>  
COPY src ./src  
RUN mvn -e -B package  
CMD ["java", "-jar", "app/app.jar"]

### #11: 使用多阶段构建来删除构建依赖关系

FROM maven:3.6-jdk-8-alpine<font color=green> AS builder</font>  
WORKDIR /app  
COPY pom.xml  
RUN mvn -e -B dependency:resolve  
COPY src ./src  
RUN mvn -e -B package  
<font color=red>~~CMD ["java", "-jar", "/app/app.jar"]~~</font>

<font color=green>
FROM openjdk:8-jre-alpine

COPY --from=builder /app/target/app.jar /  
CMD ["java", "-jar", "/app.jar"]
</font>


