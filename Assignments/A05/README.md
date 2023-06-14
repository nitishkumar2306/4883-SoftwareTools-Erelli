## Project Title : FamilyTree via Graphviz
### Name : Nitish Kumar Erelli
## Project Description : 
This project aims to generate a family tree graph programmatically using GraphViz. The goal is to create a comprehensive family tree with a minimum of 7-10 generations. Each family will be associated with a clan, and each clan will be assigned a unique color for easy identification.

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

