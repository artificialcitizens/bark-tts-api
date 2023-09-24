# Bark AI MicroService

A micro service for running Suno's [Bark](https://github.com/suno-ai/bark) model for text to speech generation.
Built to interface with the [acai.so](https://www.acai.so) AI toolkit for powering text to speech capabilities from your own compute.

You can run this via API for any UI you'd like to build out

## Prerequisites

You will need the following tools:

- Python 3.9
- pip (Python package installer)
- Miniconda (Recommended)

## Setup

### Step 1

Clone the repository

```bash
git clone bark-service
```

### Step 2

Navigate to the project directory

```bash
cd bark-service
```

### Step 3 (Recommended)

We recommend using Miniconda to create an isolated Python environment for this project. If you haven't installed Miniconda yet, you can download it from [here](https://docs.conda.io/en/latest/miniconda.html).

Create a new conda environment with Python 3.9

```bash
conda create -n myenv python=3.9
```

Activate the conda environment

```bash
conda activate myenv
```

### Step 4

Install the required packages using pip

```bash
pip install --no-cache-dir -r requirements.txt
```

## Docker Compose Setup

This project includes a `docker-compose.yml` file that can be used to create a Docker container for the application. Here are the steps to use Docker Compose:

### Prerequisites

You will need the following tools:

- Docker
- Docker Compose

### Step 1

Clone the repository

```bash
git clone <repository-url>
```

### Step 2

Navigate to the project directory

```bash
cd /path/to/project
```

### Step 3

Build and run the Docker container using Docker Compose

```bash
docker-compose up --build
```

The application will start running at http://0.0.0.0:5000

To stop the application, press `Ctrl+C`. To remove the Docker container, run `docker-compose down`.

## Running the Application

Run the application with the following command:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 5000
```

The application will start running at http://0.0.0.0:5000

## Bark Model

The suno bark model will begin downloading from [Huggingface](https://huggingface.co/collections/suno/bark-6502bdd89a612aa33a111bae) when the server is started if you don't have them cached

Once downloaded they will load into GPU memory. The `suno/bark` model uses ~5.5gb of VRAM while the `suno/bark-small` uses ~2.25gb. 

We recommend the standard model for best quality

## Calling the API

This application provides an API endpoint that you can use to run inference and get an audio response. Here is how you can call it:

### `POST /bark-inference`

This endpoint accepts a JSON object with the following properties:

- `text` (string): The text to be converted to speech.
- `voice` (string, optional): The voice preset to be used in the speech synthesis

The endpoint returns an audio file in WAV format.

#### Example

Here is an example of how to call this endpoint using Python's `requests` library:

```python
import requests
import json

url = "http://0.0.0.0:5000/bark-inference"
data = {
    "text": "Hello, world!",
    "voice": "en-US"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

# The response will be an audio file in WAV format.
with open('output.wav', 'wb') as out_file:
    out_file.write(response.content)
```

You can then play the `output.wav` file to hear the synthesized speech.

## Using Axios (Node.js)

You can use the `axios` package in Node.js to make a POST request to the API:

```javascript
const axios = require('axios');
const fs = require('fs');

const data = {
  text: 'Hello, world!',
  voice: 'en-US'
};

axios.post('http://0.0.0.0:5000/bark-inference', data, { responseType: 'arraybuffer' })
  .then((response) => {
    fs.writeFileSync('output.wav', response.data);
  })
  .catch((error) => {
    console.error(error);
  });
```

## Using cURL

You can use `curl` in the command line to make a POST request to the API:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"text":"Hello, world!","voice":"en-US"}' http://0.0.0.0:5000/bark-inference --output output.wav
```

This will save the response as a WAV file named `output.wav`.

## License

This project is licensed under the MIT License.