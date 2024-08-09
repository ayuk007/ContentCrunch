<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>ContentCrunch</h1>

<p><strong>ContentCrunch</strong> is an AI-powered tool that simplifies and summarizes content from various sources like YouTube videos, blogs, or web content URLs. It leverages advanced language models and cutting-edge AI technology to provide concise and accurate summaries, saving time and enhancing productivity.</p>

<h2>Features</h2>
<ul>
    <li><strong>YouTube Summarization</strong>: Extracts and summarizes content from YouTube videos.</li>
    <li><strong>Blog/Web Content Summarization</strong>: Handles URLs of blogs and web pages to generate precise summaries.</li>
    <li><strong>AI-Powered</strong>: Utilizes the Gemma 7b model through Groq and Langchain to create accurate and coherent summaries.</li>
    <li><strong>Customizable Chains</strong>: Employs Langchain’s document loaders and LCEL for generating custom chains tailored to your content needs.</li>
    <li><strong>Streamlit Frontend</strong>: User-friendly interface built using Streamlit.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><a href="https://github.com/langchain-ai/langchain" target="_blank"><strong>Langchain</strong></a>: A powerful framework for developing applications using large language models.</li>
    <li><a href="https://www.groq.com/" target="_blank"><strong>Groq</strong></a>: A platform that provides high-performance computing for AI models.</li>
    <li><strong>Gemma 7b Model</strong>: A cutting-edge language model used for generating summaries.</li>
    <li><strong>LCEL</strong>: Langchain Execution Logic (LCEL) for chain generation, enhancing the flexibility and effectiveness of content processing.</li>
    <li><a href="https://streamlit.io/" target="_blank"><strong>Streamlit</strong></a>: A framework for building interactive web applications with Python.</li>
</ul>

<h2>Token Limit Considerations</h2>
<p>Due to the token limit of the Gemma 7b model, the amount of content that can be summarized in one go is restricted. This is a known limitation of the current version of <strong>ContentCrunch</strong>. We are actively exploring solutions to overcome this limitation, such as content chunking or using alternative models for larger inputs.</p>

<h2>Installation</h2>
<p>To get started with <strong>ContentCrunch</strong>, follow these steps:</p>
<ol>
    <li><strong>Clone the repository</strong>:
        <pre><code>git clone https://github.com/ayuk007/ContentCrunch.git
cd ContentCrunch</code></pre>
    </li>
    <li><strong>Install the required dependencies</strong>:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Set up API keys and environment variables</strong>:
        <p>Ensure you have the necessary API keys for accessing Langchain and Groq services.</p>
        <p>Create a <code>.env</code> file in the root directory and add your keys:</p>
        <pre><code>LANGCHAIN_API_KEY=your_langchain_api_key
GROQ_API_KEY=your_groq_api_key</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li><strong>Run the Streamlit app</strong>:
        <pre><code>streamlit run app.py</code></pre>
    </li>
</ol>

<h2>Contributing</h2>
<p>We welcome contributions! If you would like to contribute to the project, please follow these steps:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/your-feature-name</code>).</li>
    <li>Commit your changes (<code>git commit -m 'Add your feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/your-feature-name</code>).</li>
    <li>Open a pull request.</li>
</ol>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE" target="_blank">LICENSE</a> file for more details.</p>

<h2>Acknowledgements</h2>
<ul>
    <li><a href="https://github.com/langchain-ai/langchain" target="_blank">Langchain</a> community for the robust framework.</li>
    <li><a href="https://www.groq.com/" target="_blank">Groq</a> for their high-performance AI platform.</li>
    <li>The developers and researchers behind the Gemma 7b model.</li>
</ul>

</body>
</html>
