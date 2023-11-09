"""
This program provides basic information (definition, symptoms, causes, treatment options)
about mental health conditions like depression, anxiety and ADHD

"""
# Defining a dictionary which contains information about depression, anxiety and ADHD

mental_health_conditions = {
    "depression": {
        "symptoms": ["persistent sad, anxious, or 'empty' mood",
                     "loss of interest or pleasure in activities",
                     "significant weight loss or gain",
                     "insomnia or excessive sleeping",
                     "feelings of worthlessness or guilt",
                     "difficulty concentrating or making decisions"],
        "causes": ["biological factors, such as changes in brain chemistry",
                   "psychological factors, such as a traumatic event or chronic stress",
                   "social factors, such as isolation or loss of a loved one"],
        "treatment": ["psychotherapy, such as cognitive-behavioral therapy (CBT) or interpersonal therapy",
                      "medications, such as antidepressants",
                      "lifestyle changes, such as exercise and stress management"]
    },
    "anxiety": {
        "symptoms": ["feeling restless, wound-up, or on-edge",
                     "easily fatigued",
                     "difficulty concentrating or mind going blank",
                     "irritability",
                     "muscle tension",
                     "sleep disturbance"],
        "causes": ["genetics",
                   "brain chemistry and hormones",
                   "past traumatic events",
                   "chronic medical conditions",
                   "substance abuse",
                   "poorly treated depression"],
        "treatment": ["cognitive-behavioral therapy (CBT)",
                      "medication such as selective serotonin reuptake inhibitors (SSRIs), benzodiazepines",
                      "relaxation techniques such as deep breathing, progressive muscle relaxation, yoga, tai chi"
                      "exposure therapy"
                      "mindfulness practices"]
    },
    "ADHD": {
        "symptoms": ["inattention",
                     "hyperactivity",
                     "impulsivity"],
        "causes": ["genetics",
                   "brain development",
                   "alcohol and tobacco use during pregnancy",
                   "exposure to environmental toxins",
                   "low birth weight",
                   "injuries to the brain"],
        "treatment": ["stimulant medication such as Ritalin and Adderall",
                      "non-stimulant medication such as Strattera",
                      "behavioral therapy",
                      "parenting training",
                      "educational intervention",
                      "counseling"]
    }
}


# Defining the main function for mental_health_bot

def mental_health_bot():
    # Greeting message
    print("""Hello, I am a mental health chatbot! I can help you with information about mental health disorders.
    To ask a question, follow the following keys-
    depression = 'depression'
    anxiety = 'anxiety'
    ADHD = 'ADHD'
    to quit - 'bye'
        """)
    while True:
        user_input = input()

        # Handling the case when the user inputs "depression"
        if "depression" in user_input:
            print("Depression is a common mental disorder characterized by persistent "
                  "sadness and a loss of interest in activities. Some common symptoms of depression include:")
            for symptom in mental_health_conditions["depression"]["symptoms"]:
                print("- " + symptom)
            print("Some possible causes of depression include:")
            for cause in mental_health_conditions["depression"]["causes"]:
                print("- " + cause)
            print("There are several treatment options for depression, including:")
            for treatment in mental_health_conditions["depression"]["treatment"]:
                print("- " + treatment)
        elif "anxiety" in user_input:
            # Handling the case when the user inputs "anxiety"

            print(
                "Anxiety is a feeling of unease, such as worry or fear, that can be mild or severe. "
                "Anxiety disorders form a category of mental health diagnoses. Some common symptoms of anxiety include:")
            for symptom in mental_health_conditions["anxiety"]["symptoms"]:
                print("- " + symptom)
            print("Some possible causes of anxiety include:")
            for cause in mental_health_conditions["anxiety"]["causes"]:
                print("- " + cause)
            print("There are several treatment options for anxiety, including:")
            for treatment in mental_health_conditions["anxiety"]["treatment"]:
                print("- " + treatment)
        elif "ADHD" in user_input:
            # Handling the case when the user inputs "adhd"

            print(
                "ADHD is a neurodevelopmental disorder that affects attention, hyperactivity, and impulsivity. "
                "Some common symptoms of ADHD include:")
            for symptom in mental_health_conditions["ADHD"]["symptoms"]:
                print("- " + symptom)
            print("Some possible causes of ADHD include:")
            for cause in mental_health_conditions["ADHD"]["causes"]:
                print("- " + cause)
            print("There are several treatment options for ADHD, including:")
            for treatment in mental_health_conditions["ADHD"]["treatment"]:
                print("- " + treatment)
        elif "bye" in user_input:
            # Ends the code
            print("Goodbye, I hope I was able to help you today!")
            break
        else:
            print("I'm sorry, I didn't understand what you said. Could you please rephrase that?")

mental_health_bot()
