# Azure Firewall Rule Manager

## Project Structure

- `src/`: Contains the main application code.
- `tests/`: Contains test scripts to validate the functionality.
- `README.md`: Provides an overview and instructions for the project.
- `.gitignore`: Specifies files and directories that should be ignored by Git.
## Project Overview

The **Azure Firewall Rule Manager** is a Python application designed to help manage Azure Firewall rules programmatically using the Azure SDK for Python. This project demonstrates how to interact with Azure Firewall resources, including retrieving and listing firewall rules. It serves as a starting point for developing more advanced firewall management tools and automating network security tasks in Azure.

## Features

- Connects to Azure using Azure SDK for Python.
- Retrieves and lists Azure Firewall rules for a specified firewall.
- Modular and easy to extend with additional functionality.

## Setup Instructions

### Prerequisites

- **Python 3.x**: Ensure that Python 3 is installed on your machine.
- **Azure Subscription**: You need an Azure subscription to access Azure resources.
- **Azure SDK for Python**: Required packages are listed in `requirements.txt`.

### Clone the Repository

1. Open your terminal and navigate to the directory where you want to clone the repository.
2. Run the following command to clone the repository:
    ```bash
    git clone https://github.com/your-username/azure-firewall-rule-manager.git
    ```
   Replace `your-username` with your GitHub username.

### Set Up the Environment

1. Navigate into the project directory:
    ```bash
    cd azure-firewall-rule-manager
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv env
    ```

   - Activate the virtual environment:
     - **Linux/Mac**:
       ```bash
       source env/bin/activate
       ```
     - **Windows**:
       ```bash
       .\env\Scripts\activate
       ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Azure Credentials**:
   - Ensure that you have set up Azure authentication. You can use Azure CLI or environment variables for this purpose. For more details, refer to [Azure Authentication](https://docs.microsoft.com/en-us/azure/developer/python/sdk/authenticate).

### Running the Application

1. Open the `src/main.py` file and update the following placeholders with your Azure details:
   - `"your-subscription-id"`
   - `"your-resource-group"`
   - `"your-firewall-name"`

2. Run the script to list Azure Firewall rules:
    ```bash
    python src/main.py
    ```

3. Check the output in the terminal to see the list of firewall rules.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Azure team for providing the Azure SDK for Python.
- Special thanks to the open-source community for their contributions.
