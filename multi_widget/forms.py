from django import forms
from models import DemoModel

class FeetInchesWidget(forms.MultiWidget):
    def __init__(self,attrs=None):
        # Widgets to attach to each of the sub-fields
        widgets = (
            forms.TextInput(),
            forms.TextInput()
        )
        super(FeetInchesWidget,self).__init__(widgets,attrs)

    def decompress(self,value):
        # Takes values from the database (or what have you)
        # and creates a list of vlaues to populate the
        # sub-fields of the MultiValueField.
        if type(value) == int:
            # Split the inches into feet and inches.
            # Modulus and floor division for the win.
            feet   = value/12
            inches = value%12
            return [feet,inches]
        else:
            # This is a "fresh" form, so the values
            # are still None (which isn't an int).
            return [0,0]

class FeetInchesField(forms.MultiValueField):
    def __init__(self,*args,**kwargs):
        a = kwargs.copy()

        # Sub-fields to handle the new "split" value
        a['fields'] = (
            forms.IntegerField(min_value=0,label="feet"),
            forms.IntegerField(min_value=0,max_value=11,label="inches")
        )

        # Bind this to the above widget
        a['widget'] = FeetInchesWidget()

        # Make sure we call the parent and pass on the
        # args so other options still work.
        super(FeetInchesField,self).__init__(*args,**a)

    def compress(self,data_list):
        # Gets a list of values from the sub-fields this
        # is made out of. For this example: (feet,inches)
        # so we add it up as such:
        return data_list[0]*12 + data_list[1]

class FeetInchesModelForm(forms.ModelForm):
    # Override the default IntegerField for this
    # model field and replace it with our FeetInchesField
    length = FeetInchesField(label="Length")

    class Meta:
        model = DemoModel