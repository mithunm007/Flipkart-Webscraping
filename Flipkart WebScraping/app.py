import gradio as gr
from transformers import pipeline

# Load a pre-trained model and tokenizer from Hugging Face
model_name = "deepset/roberta-base-squad2"  # This is a model fine-tuned for Q&A
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# Predefined questions and answers
qa_pairs = {
    "What are the key Acts and Rules governing the Mining Industry in India?":
        "The key Acts and Rules governing the Mining Industry in India include:\n"
        "1. The Mines and Minerals (Development and Regulation) Act, 1957\n"
        "2. The Coal Mines Act, 1952\n"
        "3. The Indian Explosives Act, 1884\n"
        "4. The Air (Prevention and Control of Pollution) Act, 1981\n"
        "5. The Water (Prevention and Control of Pollution) Act, 1974\n"
        "6. The Environment Protection Act, 1986\n"
        "7. The National Mineral Policy, 2019\n"
        "8. The Mines Act, 1952 (applicable to coal mines only)\n"
        "9. The Mineral Conservation and Development Rules, 1988\n"
        "10. The Mineral (Auction) Rules, 2020",
    "What is the purpose of the Mines and Minerals (Development and Regulation) Act, 1957?":
        "The Mines and Minerals (Development and Regulation) Act, 1957, aims to regulate the exploration, mining, and production of minerals in India. It provides for the establishment of a National Mineral Development Corporation and the Central Mining and Geological Survey Organization.",
    "How does the Air (Prevention and Control of Pollution) Act, 1981, relate to mining?":
        "The Air (Prevention and Control of Pollution) Act, 1981, sets standards for air quality and requires industries to install pollution control equipment. Mining operations can generate significant air pollution, so this act is relevant to the mining industry.",
    "What do the Water (Prevention and Control of Pollution) Act, 1974, and the Environment Protection Act, 1986, cover?":
        "The Water (Prevention and Control of Pollution) Act, 1974, sets standards for water quality and requires industries to install wastewater treatment facilities. The Environment Protection Act, 1986, aims to protect and improve the quality of the environment and requires industries to obtain environmental clearance before operating.",
    "What is the significance of the Mines Act, 1952?":
        "The Mines Act, 1952, is a legacy law that regulates the working conditions, safety, and welfare of laborers in coal mines. It has been superseded by the Mines and Minerals (Development and Regulation) Act, 1957, which applies to all minerals.",
    "How are royalties regulated in mining?":
        "Royalties are regulated by the Mines and Minerals (Development and Regulation) Act, 1957. The act sets the rates of royalty for different minerals based on their market value.",
    "Are there any forest-related laws that apply to mining?":
        "Yes, the Forest Conservation Act, 1980, and the Wildlife Protection Act, 1972, can be relevant to mining projects, particularly those located in forested areas.",
    "Where can I find more information about these laws and regulations?":
        "You can consult official government websites, legal authorities, or contact the Ministry of Mines for detailed information.",
    "How can I stay updated on changes in mining laws?":
        "It's advisable to regularly check official government websites and subscribe to relevant industry publications for updates.",
    "Is there a 24/7 chatbot available for mining industry queries?":
        "Yes, the Ministry of Mines has developed a chatbot using AI and NLP technology to answer queries related to mining laws, acts, and regulations, available 24/7.",
    "What is the National Mineral Policy, 2019, and what does it aim to achieve?":
        "The National Mineral Policy, 2019, is a comprehensive policy framework that aims to promote sustainable and responsible mining practices in India. It outlines the vision for the mining sector, including the role of the private sector, the need for technology adoption, and the importance of environmental protection and community development.",
    "How does the Mineral Conservation and Development Rules, 1988, regulate mining activities?":
        "The Mineral Conservation and Development Rules, 1988, provide guidelines for the exploration, mining, and production of minerals in India. It outlines the procedures for obtaining mining leases, the requirements for environmental clearance, and the regulations for mineral transportation.",
    "What is the Mineral (Auction) Rules, 2020, and how does it affect mining?":
        "The Mineral (Auction) Rules, 2020, provide guidelines for the auction of mining leases for minerals in India. It aims to increase transparency, efficiency, and competition in the mining sector. The rules outline the eligibility criteria for bidders, the auction process, and the terms and conditions of the mining leases.",
    # Add more questions and answers here
}

# Mining laws context for the LLM
mining_laws_context = """
The Mines and Minerals (Development and Regulation) Act, 1957, provides the legal framework for mineral exploration and mining activities. It outlines the requirements for obtaining mining licenses, the obligations of mining companies, and the rights of landowners. Key regulations include environmental protection measures, safety standards, and royalty payments. The act aims to promote sustainable and responsible mining practices.

Key Acts and Rules governing the Mining Industry in India include:
1. The Mines and Minerals (Development and Regulation) Act, 1957
2. The Coal Mines Act, 1952
3. The Indian Explosives Act, 1884
4. The Air (Prevention and Control of Pollution) Act, 1981
5. The Water (Prevention and Control of Pollution) Act, 1974
6. The Environment Protection Act, 1986
7. The National Mineral Policy, 2019
8. The Mines Act, 1952 (applicable to coal mines only)
9. The Mineral Conservation and Development Rules, 1988
10. The Mineral (Auction) Rules, 2020

The purpose of the Mines and Minerals (Development and Regulation) Act, 1957, is to regulate the exploration, mining, and production of minerals in India.

The Air (Prevention and Control of Pollution) Act, 1981, sets standards for air quality and requires industries to install pollution control equipment. Mining operations can generate significant air pollution, so this act is relevant to the mining industry.

The Water (Prevention and Control of Pollution) Act, 1974, sets standards for water quality and requires industries to install wastewater treatment facilities. The Environment Protection Act, 1986, aims to protect and improve the quality of the environment and requires industries to obtain environmental clearance before operating.

The Mines Act, 1952, is a legacy law that regulates the working conditions, safety, and welfare of laborers in coal mines. It has been superseded by the Mines and Minerals (Development and Regulation) Act, 1957, which applies to all minerals.

The act sets the rates of royalty for different minerals based on their market value.

Forest-related laws like the Forest Conservation Act, 1980, and the Wildlife Protection Act, 1972, can be relevant to mining projects, particularly those located in forested areas.

The National Mineral Policy, 2019, is a comprehensive policy framework that aims to promote sustainable and responsible mining practices in India. It outlines the vision for the mining sector, including the role of the private sector, the need for technology adoption, and the importance of environmental protection and community development.

The Mineral Conservation and Development Rules, 1988, provide guidelines for the exploration, mining, and production of minerals in India. It outlines the procedures for obtaining mining leases, the requirements for environmental clearance, and the regulations for mineral transportation.

The Mineral (Auction) Rules, 2020, provide guidelines for the auction of mining leases for minerals in India. It aims to increase transparency, efficiency, and competition in the mining sector. The rules outline the eligibility criteria for bidders, the auction process, and the terms and conditions of the mining leases.

For more information about these laws and regulations, you can consult official government websites, legal authorities, or contact the Ministry of Mines for detailed information.

To stay updated on changes in mining laws, it's advisable to regularly check official government websites and subscribe to relevant industry publications for updates.

The Ministry of Mines has developed a chatbot using AI and NLP technology to answer queries related to mining laws, acts, and regulations, available 24/7.
"""

# Function to handle user queries
def ask_mining_law(question):
    # Check if the question matches a predefined one (case-insensitive match)
    for predefined_question, answer in qa_pairs.items():
        if predefined_question.lower() in question.lower():
            return answer
    # If the question seems to be about mining laws but isn't predefined, use the LLM
    if "mining" in question.lower() or "law" in question.lower() or "regulation" in question.lower():
        result = nlp(question=question, context=mining_laws_context)
        return result['answer']
    # Default response for irrelevant questions
    return "I'm sorry, I can only answer questions related to mining laws and regulations. Please ask a relevant question."

# Create the Gradio interface
iface = gr.Interface(
    fn=ask_mining_law,
    inputs="text",
    outputs="text",
    title="Mining Law Bot",
    description="""
    <div style="text-align: center;">
        <img src="https://shorturl.at/qgerV" alt="Mining Law" style="max-width:100%;height=auto;">
    </div>
    <p>Ask any question about mining laws and regulations.</p>
    <p>Here are some example questions you can ask:</p>
    <ul style="text-align:left;">
        <li>What are the key Acts and Rules governing the Mining Industry in India?</li>
        <li>What is the purpose of the Mines and Minerals (Development and Regulation) Act, 1957?</li>
        <li>How does the Air (Prevention and Control of Pollution) Act, 1981, relate to mining?</li>
        <li>What do the Water (Prevention and Control of Pollution) Act, 1974, and the Environment Protection Act, 1986, cover?</li>
        <li>What is the significance of the Mines Act, 1952?</li>
        <li>How are royalties regulated in mining?</li>
        <li>Are there any forest-related laws that apply to mining?</li>
        <li>Where can I find more information about these laws and regulations?</li>
        <li>How can I stay updated on changes in mining laws?</li>
        <li>Is there a 24/7 chatbot available for mining industry queries?</li>
        <li>What is the National Mineral Policy, 2019, and what does it aim to achieve?</li>
        <li>How does the Mineral Conservation and Development Rules, 1988, regulate mining activities?</li>
        <li>What is the Mineral (Auction) Rules, 2020, and how does it affect mining?</li>
    </ul>
    """
)

# Launch the interface
iface.launch(share=True)
