import csv


def generate_dot_file(csv_file, dot_file):
  # Read the CSV file
  with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)

  # Create the DOT file
  with open(dot_file, 'w') as file:
    file.write('digraph FamilyTree {\n')

    # Create a dictionary to store the gender shapes
    gender_shapes = {'M': 'square', 'F': 'circle'}

    # Create a dictionary to store the clan colors
    clan_colors = {
      '1': '#cfeeff',  # Light blue
      '2': '#d9f6d4',  # Light green
      '3': '#fff9c4',  # Light yellow
      '4': '#f8bbd0',  # Light pink
      '5': '#ffccbc',  # Light salmon
      '6': '#e0e0e0',  # Light gray
      '7': '#e0f7fa'  # Light cyan
    }
    clan_names = {
      '1': 'Longbeards',
      '2': 'Firebeards',
      '3': 'Broadbeams',
      '4': 'Ironfists',
      '5': 'Stiffbeards',
      '6': 'Stonefoots',
      '7': 'Blacklocks'
    }

    # Write DOT file configurations
    file.write('\tnode [shape=box, style="filled"];')
    file.write(
      '\tedge [fontname="Helvetica", color="#333333", penwidth="2.0"];'
    )  # Set edge color to dark gray and penwidth to 2.0
    file.write('\tnode [fontname="Helvetica"];')
    file.write(
      '\trankdir = TB;  // Set the rank direction to left-to-right\n\n')

    file.write('\t{rank=same; 0; 1;}\n')
    file.write('\t{rank=same; 2; 3;}\n')

    # Set the position for 0th generation individuals
    file.write('\tpos="0,0!"\n\n')

    file.write('\t// Define the nodes\n')

    for row in rows:
      pid = row['pid']
      name = row['name']
      gender = row['gender']
      generation = row['generation']
      byear = row['byear']
      dyear = row['dyear']
      dage = row['dage']
      myear = row['myear']
      mage = row['mage']
      ptype = row['ptype']
      clan_id = row['clan']
      spouse_id = row['spouseId']
      parent_id1 = row['parentId1']
      parent_id2 = row['parentId2']
      parent_node_id = row['parentNodeId']

      # Determine the shape for the current gender
      shape = gender_shapes.get(gender, 'rectangle')

      # Determine the color for the current clan
      clan_color = clan_colors.get(clan_id, 'white')
      clan_name = clan_names.get(clan_id, '')

      # Write the node information with the shape based on gender and clan color
      file.write(
        f'\t{pid} [label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4">'
        f'<TR><TD ALIGN="LEFT"><B>{name}</B></TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Gender: </B> {gender}</TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Generation: </B> {generation}</TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Clan:</B> {clan_name}</TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Birth Year: </B> {byear}</TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Death Year: </B> {dyear}</TD></TR>'
        f'<TR><TD ALIGN="LEFT"><B>Age: </B> {dage}</TD></TR>'
        f'</TABLE>> shape="{shape}", style="filled", fillcolor="{clan_color}", fontcolor="black"];\n'
      )

      # Write the edge information for parents
      if parent_id1 and parent_id1 != spouse_id:
        file.write(
          f'\t{parent_id1} -> {pid} [label="Child", color="#333333", penwidth="2.0"];\n'
        )  # Dark gray edge color and thicker penwidth
      if parent_id2 and parent_id2 != spouse_id:
        file.write(
          f'\t{parent_id2} -> {pid} [label="Child", color="#333333", penwidth="2.0"];\n'
        )  # Dark gray edge color and thicker penwidth

      # Write the edge information for parent node
      if parent_node_id and parent_node_id != spouse_id:
        file.write(
          f'\t{parent_node_id} -> {pid} [label="Child", color="#333333", penwidth="2.0"];\n'
        )  # Dark gray edge color and thicker penwidth

      # Store the couple information
      if spouse_id:
        if gender == "M":
          file.write(
            f'\t{pid} -> {spouse_id} [label="Husband", color="#333333", penwidth="2.0"];\n'
          )  # Dark gray edge color and thicker penwidth
          file.write(
            f'\t{spouse_id} -> {pid} [label="Wife", color="#333333", penwidth="2.0"];\n'
          )  # Dark gray edge color and thicker penwidth
        elif gender == "F":
          file.write(
            f'\t{pid} -> {spouse_id} [label="Wife", color="#333333", penwidth="2.0"];\n'
          )  # Dark gray edge color and thicker penwidth
          file.write(
            f'\t{spouse_id} -> {pid} [label="Husband", color="#333333", penwidth="2.0"];\n'
          )  # Dark gray edge color and thicker penwidth

    file.write('}')


# Call the function with the CSV and DOT file paths
csv_file = 'family_tree_data.csv'
dot_file = 'family_tree.dot'
generate_dot_file(csv_file, dot_file)
