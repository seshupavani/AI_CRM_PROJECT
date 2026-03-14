hcp_database=[
"Dr Sharma",
"Dr Kumar",
"Dr Smith",
"Dr Patel",
"Dr Reddy"
]

def search_hcp(query:str):

    return[
        hcp for hcp in hcp_database
        if query.lower() in hcp.lower()
    ]