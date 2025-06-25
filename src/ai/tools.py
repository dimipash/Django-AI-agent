from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool

from documents.models import Document


@tool
def list_documents(config: RunnableConfig):
    """
    List the most recent LIMIT documents for the current user with maximum of 25.

    agruments
    limit: number of results
    """
    print(config)
    metadata = config.get("metadata") or config.get("configurable")
    user_id = metadata.get("user_id")
    if not user_id:
        raise Exception("User not found")
    print(user_id)
    qs = Document.objects.filter(owner_id=user_id, active=True)
    response_data = []
    for obj in qs:
        response_data.append({"id": obj.id, "title": obj.title})

    return response_data


@tool
def get_document(document_id: int, config: RunnableConfig):
    """
    Get the details of a document for the current user
    """
    metadata = config.get("metadata") or config.get("configurable")
    user_id = metadata.get("user_id")
    if not user_id:
        raise Exception("User not found")

    try:
        obj = Document.objects.get(id=document_id, owner_id=user_id, active=True)
    except Document.DoesNotExist:
        raise Exception("Document not found")
    except:
        raise Exception("Something went wrong")
    
    response_data = {"id": obj.id, "title": obj.title}

    return response_data
