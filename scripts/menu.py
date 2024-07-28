import inquirer
import json

def get_user_input():
    questions = [
        inquirer.Text('url', message="Enter the target website URL"),
        inquirer.List('user_agent', message="Choose a user-agent", choices=[
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
        ]),
        inquirer.List('proxy', message="Choose a proxy", choices=[
            "http://192.168.1.100:8080",
            "http://192.168.1.101:8080",
            "http://192.168.1.102:8080"
        ])
    ]

    answers = inquirer.prompt(questions)
    return answers

