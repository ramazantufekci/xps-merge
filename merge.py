from aspose.page.xps import * 

# Define the working directory.
data_dir =  "./files"
# Initialize the XPS output stream
with open(data_dir + "mergedXPSfiles.xps", "wb") as out_stream:
    # Load XPS document from the file by instantiating an instance of the XpsDocument class. 
    document = XpsDocument(data_dir + "input.xps", XpsLoadOptions())
    # Define an array of XPS files which will be merged with the first one.
    files_to_merge = [ data_dir + "Demo.xps", data_dir + "sample.xps" ]
    # Invoke the merge method to merge the XPS files. 
    document.merge(files_to_merge, out_stream)
