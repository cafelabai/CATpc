### Overview

This repository presents a strategy to generate a culturally responsive dataset for fine-tuning a Large Language Model (LLM) tailored for K12 STEM education. Our approach uses a combination of prompt engineering and careful data segmentation to extract meaningful question-answer pairs from a PDF document, focusing on culturally relevant pedagogy.

### Strategy Alignment with the Code

1. **Text Extraction and Metadata Analysis**: 
   The code begins by using `UnstructuredPDFLoader` to extract the text content and metadata from a provided PDF document. This step is crucial in understanding the structure and nature of the document. For this project, we load a PDF which contains documents created by  team members who have consolidated their learnings from diverse research papers. This PDF is loaded to extract meaningful text segments that can form the basis for creating Q&A pairs relevant to culturally responsive teaching.

2. **Text Segmentation Techniques**:
   We utilize two segmentation methods: 
   - **Fixed-Size Segmentation**: Dividing text into fixed-size segments allows for an initial, structured approach to managing content size, ensuring that each segment is neither too short nor too long.
   - **Sliding Window Segmentation**: This technique introduces overlapping segments to ensure continuity in context, making it more likely that key ideas are retained and well-represented in the Q&A pairs.

3. **Prompt Engineering for Q&A Generation**:
   Leveraging the `OllamaFunctions` LLM model, the script is designed to generate questions that prompt the LLM to focus on key ideas from the text that align with multicultural and inclusive teaching practices. The model is further used to extract answers, ensuring they are directly derived from the text.

4. **Data Cleaning and Export**:
   The generated questions and answers are aggregated into structured pairs, which are then saved into a JSON file with an option to convert them into CSV for easier integration. This structured dataset is pivotal for future fine-tuning or use in educational settings. We aim to create a dataset that reflects diverse voices and inclusive practices in a way that can be used by educators and researchers to support culturally responsive pedagogy.

### Implementation Steps

#### 1. Install Ollama

Visit the [Ollama website](https://ollama.com) to download and install the Ollama CLI tool. Follow the instructions provided on the website for your operating system.

#### 2. Install Required Packages

Install the required Python packages using pip:

```sh
pip install langchain_community langchain_experimental ollama pydantic json csv
```

Ensure that Python (version 3.8 or higher) is installed on your system.

#### 3. Clone the Repository

Clone this GitHub repository to your local machine:

```sh
git clone https://github.iu.edu/sunchak/CATpc.git
cd "CATpc\Dataset Preparation"
```

#### 4. Prepare the PDF File

Place the `Summaries.pdf` file, or any other PDF file containing the source text, in the root directory of the repository.

#### 5. Execute the Script

Run the script by executing the following command:

```sh
python pdfExt.py
```

#### 6. Review and Export the Output

The script will generate a JSON file named `final_dataset.json` containing the Q&A pairs. To convert this file to CSV format, run:

```sh
python your_script_name.py --convert-json-to-csv
```

## Next Steps

We continue working on creating better summaries, refining the model prompts, and segmentation strategies to further align with the goals of culturally responsive pedagogy. Our ongoing feedback loop with educational experts ensures that the generated dataset remains relevant, diverse, and impactful in promoting multicultural inclusivity in STEM learning.