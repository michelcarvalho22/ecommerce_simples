from django import forms


class FormProduto(forms.Form):

    cor = forms.CharField(label='Cor',required=False)
    tamanho = forms.CharField(label='Tamanho',required=False)

    def __init__(self,*args,**kwargs):
        super(FormProduto,self).__init__(*args,**kwargs)


class FormBuscaProduto(forms.Form):

    descricao = forms.CharField(label='Descrição',required=False)

    def __init__(self,*args,**kwargs):
        super(FormBuscaProduto,self).__init__(*args,**kwargs)



