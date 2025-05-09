# tools/csv_tools.py

from server import mcp
from utils.file_reader import read_csv_summary, read_csv_column_names 
#from mcp.server.decorators import tool

@mcp.tool()
def summarize_csv_file(filename: str) -> str:
    """
    Summarize a CSV file by reporting its number of rows and columns.
    Args:
        filename: Name of the CSV file in the /data directory (e.g., 'sample.csv')
    Returns:
        A string describing the file's dimensions.
    """
    return read_csv_summary(filename)

@mcp.tool()
def get_csv_column_names(filename: str) -> list[any]:
    """
    Reads the first line of a CSV file and returns the column names.
    
    Args:
        path: Path to the CSV file
        
    Returns:
        List of column names from the CSV header
    """
    return read_csv_column_names(filename)