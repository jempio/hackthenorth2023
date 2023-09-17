import axios from 'axios';

const handleChatRequest = async () => {
  try {
    const apiKey = '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';
    const question = 'Give me a easy-to-prunounce English sentence, around 7 words. Keep your answer to just that one sentence';
    const url = 'https://api.openai.com/v1/engines/text-davinci-001/completions';

    const response = await axios.post(
      url,
      {
        prompt: question,
        max_tokens: 50,
      },
      {
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${apiKey}`,
        },
      }
    );

    const answer = response.data.choices[0].text;
    return answer;
  } catch (error) {
    console.error('Error fetching data:', error);
    console.error('Error data:', error.response.data);
    throw error;
  }
};

export default handleChatRequest;