import bpy

def bake_textures(object, size):
  """
  Bake Diffuse, Roughness, Normal, and Emission textures for an object.

  Args:
      object: The object to bake textures for.
      size: The desired size of the baked textures.
  """
  # Loop through each bake type
  for bake_type in ['DIFFUSE', 'ROUGHNESS', 'NORMAL', 'EMIT']:
    # Create a new image for the baked texture
    image_name = object.name + "_" + bake_type + ".png"
    image = bpy.data.images.new(image_name, width=size, height=size)

    # Set bake settings
    bpy.context.scene.render.bake = True
    bpy.context.scene.render.bake_type = bake_type
    slot = object.material_slots[0]  # Assuming single material slot
    active_node = slot.material.node_tree.nodes.active
    bpy.context.view_layer.objects.active = object

    # Set color space based on bake type
    if bake_type == 'DIFFUSE':
      active_node.image.color_space = 'SRGB'
    else:
      active_node.image.color_space = 'NON_COLOR'

    # Bake the texture
    bpy.ops.object.bake(filepath=image.filepath)

    # Clear bake settings
    bpy.context.scene.render.bake = False

# Get active object and desired texture size
active_object = bpy.context.active_object
texture_size = 1024  # You can adjust this value

# Bake textures
if active_object and active_object.type == 'MESH':
  bake_textures(active_object, texture_size)
else:
  print("Please select a mesh object to bake textures for.")


