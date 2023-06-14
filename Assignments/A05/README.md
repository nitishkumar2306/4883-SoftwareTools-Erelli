## Project Title : FamilyTree via Graphviz
### Name : Nitish Kumar Erelli
## Project Description : 
This project aims to generate a family tree graph programmatically using GraphViz. The goal is to create a comprehensive family tree with a minimum of 7-10 generations. Each family will be associated with a clan, and each clan will be assigned a unique color for easy identification.

## Gender Representation

- The **square shape** represents male individuals.
- The **circle shape** represents female individuals.

## Clan Colors

The following colors are used to represent different clans in the family tree:

- Clan 1: Light blue
- Clan 2: Light green
- Clan 3: Light yellow
- Clan 4: Light pink
- Clan 5: Light salmon
- Clan 6: Light gray
- Clan 7: Light cyan

## Generating the Family Tree Visualization

To generate the family tree visualization, follow these steps:

1. Install Graphviz: Make sure you have Graphviz installed on your machine.
2. Prepare the CSV Data: Create a CSV file containing the family tree data. Each row should represent an individual with the required information.
3. Run the Python Script: Execute the `generate_dot_file()` function in the provided Python script, passing the CSV file path and the desired output DOT file path as arguments.
4. Generate the Image: Use Graphviz to generate the image file (e.g., PNG, SVG) from the DOT file.
5. Visualize the Family Tree: Open the generated image file to view the family tree visualization.

Feel free to customize the CSV data and the Graphviz configurations to suit your specific family tree visualization needs.



## Requirements
- Python 3.x
- GraphViz

## Installation
1. Clone the repository to your local machine:
2. Navigate to the project directory:
git clone https://github.com/your-username/family-tree-generator.git

## Usage
1. Customize the family tree data:
- Open the `family_data.csv` file.
- Edit or replace the existing data with your own family tree information.
- Ensure that each family member is assigned to a clan.
2. Generate the family tree graph:
- Run the following command to generate the DOT file:
  ```
  python generate_family_tree.py
  ```
- This will create a `family_tree.dot` file in the project directory.
3. Visualize the family tree:
- Use GraphViz to convert the DOT file into an image:
- The family tree graph will be saved as `family_tree.png` in the project directory.

## Example Family Tree



## Customization
- To customize the appearance of the family tree, you can modify the `generate_family_tree.py` file. Look for the styling options within the code and make the necessary changes.
- You can also explore additional options and features provided by GraphViz to enhance the visualization of the family tree.

## Resources
- [GraphViz Documentation](https://graphviz.org/documentation/)
- [Python GraphViz Library](https://pypi.org/project/graphviz/)

