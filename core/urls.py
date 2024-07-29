from django.urls import path, include
#foi feito o importe do include acima 

#import das views index e contato criadas no core/views
from core.views import index, contato, produtos, produto_single, blogs, blog_single, camisas, camisas_single

        
urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('produtos', produtos, name='produtos'),
    path('produto/<int:id>/', produto_single, name='produto_single'),
    path('blogs', blogs, name='blogs'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
    path('camisas', camisas, name='camisas'),
    path('camisas/<slug:slug>/', camisas_single, name='camisas_single'),
    
]

# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato

