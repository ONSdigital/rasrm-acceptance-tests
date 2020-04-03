FROM python:3.6

WORKDIR /opt/build/

# Install Firefox
RUN echo "deb http://http.debian.net/debian/ unstable main contrib non-free" > /etc/apt/sources.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends firefox

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    apt-get update && \
    apt-get install -y make && \
    apt-get install -y google-chrome-stable && \
    pip install pipenv

COPY . .
RUN pipenv install --dev