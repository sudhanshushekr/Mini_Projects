




/*
 * Install the Generative AI SDK
 *
 * $ npm install @google/generative-ai
 *
 * See the getting started guide for more information
 * https://ai.google.dev/gemini-api/docs/get-started/node
 */

const {
    GoogleGenerativeAI,
    HarmCategory,
    HarmBlockThreshold,
  } = require("@google/generative-ai");
  
  const apiKey ="AIzaSyC_TpnLS3_XxioWJUZlLjtV4wxZqQgXPLg";
  const genAI = new GoogleGenerativeAI(apiKey);
  
  const model = genAI.getGenerativeModel({
    model: "gemini-1.5-flash",
  });
  
  const generationConfig = {
    temperature: 1,
    topP: 0.95,
    topK: 64,
    maxOutputTokens: 8192,
    responseMimeType: "text/plain",
  };
  
  async function run(prompt) {
    const safetySettings = [
        {
          category: HarmCategory.HATE_SPEECH,
          threshold: HarmBlockThreshold.LOW,

        }
        {
          category: HarmCategory.HARASSMENT,
          threshold: HarmBlockThreshold.LOW,
        }

        {
          category: HarmCategory.SEXUALLY_EXPLICIT,
          threshold: HarmBlockThreshold.LOW,
          
        }
      ]
    const chatSession = model.startChat({
      generationConfig,
      safetySettings,

      
   // safetySettings: Adjust safety settings
   // See https://ai.google.dev/gemini-api/docs/safety-settings
      history: [
      ],
    });
  
    const result = await chatSession.sendMessage(prompt);
    const response = result.response;
    console.log(result.response.text());
  }
  
  export default runChat();
  


  
