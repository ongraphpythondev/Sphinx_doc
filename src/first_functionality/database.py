"""
Database Functionalities
------------------------
Database is very crutial thing in and project
"""

class Databse:
    """
    Database class is responsible for connecting with database
    """

    def __init__(self , connection_string):
        """
        this connection string is used to connect with sql server
        Args:
            connection_string: This is connection string

        """
        self.connection_string = connection_string

    
    def connect(self , username : str , password : str , port : int) -> str:
        """
        this method is used to connect database

        Args:
            username(str): This is username
            password(str): This is password
            port(int): This is port
        
        Returns:
            str: returning string
        """
        return f"this is run on port no.{port}"