class UsuarioForm(forms.ModelForm):  #form.ModelForm é para banco de dados
    class Meta:
        widgets = {  #html
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }

        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password': 'Senha',
            'age': 'idade',
            'phone': 'Telefone',
        }