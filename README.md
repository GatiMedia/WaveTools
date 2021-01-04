# WaveTools

**This is a public collection of Nuke's native nodes that are**
**utilizing different types of Wave Expressions.**

[For more info](https://www.gatimedia.co.uk/wave-expression-tools)

HOW TO INSTALL:
1. Unzip the archive
  
2. Drag and drop the folder in your .nuke folder

[How to find your .nuke folder](https://support.foundry.com/hc/en-us/articles/207271649-Q100048-Nuke-Directory-Locations)

3. Add this code to your file init.py (if you don’t have it, create one) and modify the WaveTools_path.

```python
WaveTools_path = "<path to your .nuke folder>/WaveTools-main"
nuke.pluginAddPath(WaveTools_path)
```

4. Run Nuke
