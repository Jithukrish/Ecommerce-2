from django import template
register=template.Library()
@register.simple_tag(name="multiply")
# def chunks(list_data,chunk_size):
#     chunk=[]
#     i=0
#     for data in list_data:
#         chunk.append(data)
#         i=i+1
#         if i==chunk_size:
#             yield chunk
#             chunk=[]
#     yield chunk
def multiply(a,b):
    return a*b

