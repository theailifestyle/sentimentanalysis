# Sentiment Analysis App

This application provides sentiment analysis using OpenAI's GPT model.

## Setup

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/your-username/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

4. Access the application at `http://localhost:3000`

## Usage
Enter text in the input field and click "Analyze Sentiment" to get a sentiment analysis.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)