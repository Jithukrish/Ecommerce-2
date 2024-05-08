from django import template
register=template.Library()
@register.simple_tag(name="gettotal")
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
def gettotal(cart):
    total=0
    for item in  cart.added_items.all():
        total+=item.quantity*item.product.price
    return total

