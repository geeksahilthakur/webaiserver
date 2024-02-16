import openai
import time

import requests

openai.api_key = "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"

topics = [
    "Artificial Intelligence (AI)",
    "Cybersecurity",
    "Quantum Computing",
    "5G Technology",
    "Internet of Things (IoT)",
    "Blockchain",
    "Virtual Reality (VR)",
    "Augmented Reality (AR)",
    "Cryptocurrency",
    "Machine Learning",
    "Data Privacy",
    "Cloud Computing",
    "Edge Computing",
    "Robotics",
    "Autonomous Vehicles",
    "Big Data",
    "Wearable Technology",
    "Biotechnology",
    "Nanotechnology",
    "Green Technology",
    "Smart Home Devices",
    "Digital Transformation",
    "3D Printing",
    "Smart Cities",
    "Genetic Engineering",
    "Space Exploration",
    "Bioinformatics",
    "Renewable Energy",
    "Internet Security",
    "Telemedicine",
    "Remote Work",
    "Quantum Cryptography",
    "Facial Recognition",
    "Chatbots",
    "Cognitive Computing",
    "Neural Networks",
    "Predictive Analytics",
    "Voice Assistants",
    "Quantum Internet",
    "Automation",
    "Supply Chain Technology",
    "Precision Agriculture",
    "Cyber Defense",
    "Autonomous Drones",
    "FinTech",
    "RegTech",
    "InsurTech",
    "Agritech",
    "Health Informatics",
    "Digital Payments",
    "Smart Grids",
    "Smart Farming",
    "Precision Medicine",
    "Renewable Resources",
    "Cyber Intelligence",
    "Digital Currency",
    "Quantum Sensors",
    "Autonomous Robots",
    "Cloud Security",
    "Data Analytics",
    "Space Tourism",
    "Humanoid Robots",
    "Brain-Computer Interface",
    "Quantum Programming",
    "Network Security",
    "Cyber Warfare",
    "Dark Web",
    "4D Printing",
    "Energy Storage",
    "Neurotechnology",
    "Robotic Process Automation (RPA)",
    "Digital Twins",
    "Data Science",
    "Cyber Insurance",
    "Cyber Forensics",
    "Cyber Law",
    "Biometrics",
    "Clean Energy",
    "Edge AI",
    "Genetic Editing",
    "IoT Security",
    "Blockchain in Supply Chain",
    "Space Mining",
    "Cyber Physical Systems",
    "Autonomous Navigation",
    "Quantum Communication",
    "Edge Devices",
    "Quantum Algorithms",
    "Digital Identity",
    "Smart Transportation",
    "Blockchain Governance",
    "Cyber Hygiene",
    "Drone Delivery",
    "Cyber Espionage",
    "Quantum Key Distribution",
    "Sustainable Technology",
    "Autonomous Vehicles Regulation",
    "Quantum Sensing",
    "Genetic Testing",
    "Quantum Error Correction"
]

imgs= [
    "Artificial Intelligence (AI)",
    "Cybersecurity",
    "Quantum Computing",
    "5G Technology",
    "Internet of Things (IoT)",
    "Blockchain",
    "Virtual Reality (VR)",
    "Augmented Reality (AR)",
    "Cryptocurrency",
    "Machine Learning",
    "Data Privacy",
    "Cloud Computing",
    "Edge Computing",
    "Robotics",
    "Autonomous Vehicles",
    "Big Data",
    "Wearable Technology",
    "Biotechnology",
    "Nanotechnology",
    "Green Technology",
    "Smart Home Devices",
    "Digital Transformation",
    "3D Printing",
    "Smart Cities",
    "Genetic Engineering",
    "Space Exploration",
    "Bioinformatics",
    "Renewable Energy",
    "Internet Security",
    "Telemedicine",
    "Remote Work",
    "Quantum Cryptography",
    "Facial Recognition",
    "Chatbots",
    "Cognitive Computing",
    "Neural Networks",
    "Predictive Analytics",
    "Voice Assistants",
    "Quantum Internet",
    "Automation",
    "Supply Chain Technology",
    "Precision Agriculture",
    "Cyber Defense",
    "Autonomous Drones",
    "FinTech",
    "RegTech",
    "InsurTech",
    "Agritech",
    "Health Informatics",
    "Digital Payments",
    "Smart Grids",
    "Smart Farming",
    "Precision Medicine",
    "Renewable Resources",
    "Cyber Intelligence",
    "Digital Currency",
    "Quantum Sensors",
    "Autonomous Robots",
    "Cloud Security",
    "Data Analytics",
    "Space Tourism",
    "Humanoid Robots",
    "Brain-Computer Interface",
    "Quantum Programming",
    "Network Security",
    "Cyber Warfare",
    "Dark Web",
    "4D Printing",
    "Energy Storage",
    "Neurotechnology",
    "Robotic Process Automation (RPA)",
    "Digital Twins",
    "Data Science",
    "Cyber Insurance",
    "Cyber Forensics",
    "Cyber Law",
    "Biometrics",
    "Clean Energy",
    "Edge AI",
    "Genetic Editing",
    "IoT Security",
    "Blockchain in Supply Chain",
    "Space Mining",
    "Cyber Physical Systems",
    "Autonomous Navigation",
    "Quantum Communication",
    "Edge Devices",
    "Quantum Algorithms",
    "Digital Identity",
    "Smart Transportation",
    "Blockchain Governance",
    "Cyber Hygiene",
    "Drone Delivery",
    "Cyber Espionage",
    "Quantum Key Distribution",
    "Sustainable Technology",
    "Autonomous Vehicles Regulation",
    "Quantum Sensing",
    "Genetic Testing",
    "Quantum Error Correction"
]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def search_and_get_image_url(query, access_key):
    url = f"https://api.unsplash.com/photos/random/?query={query}&client_id={access_key}&count=1"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        if data:
            image_url = data[0]['urls']['full']  # Extract URL of the first image
            return image_url
        else:
            print("No images found for the query:", query)
            return None
    except requests.RequestException as e:
        print("Error fetching image:", e)
        return None

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~








def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print("An error occurred:", str(e))
        return "Sorry, something went wrong."



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    for topic, img in zip(topics, imgs):
        access_key = 'fZ2rZc6HMDHDUgSlvYm_4gj_xkLENBi8fZv7DbM0eg8'  # Replace with your Unsplash access key
        query = img
        image_url = search_and_get_image_url(query, access_key)
        if image_url:
            print("Image URL:", image_url)
        user_input = f"Write a 50-word blog post on {topic}. Include a catchy title and description."
        print("You:", user_input)
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
        time.sleep(10)  # Adjust sleep time as needed

