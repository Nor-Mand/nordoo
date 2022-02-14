# Definition of Reports
1. Create a folder reports and declare in the manifest file


### `Attributes`
- name: (mandatory)
- model: (Id of model)
- report_type: take to values(qweb-pdf, qweb-html)
- report_name:(external_id)
- print_report_name: name of report
- binding_model_id:
  - model_model_name
- paperformat_id:

#### `template`
````
<template id="report_form_card"> --> Id template
    <t t-call="web.html_container"> --> doc html
        <t t-foreach="docs" t-as="o"> --> loop of model
            <t t-call="web.external_layout"> --> header and footer
                ...
            </t>
        </t>
    </t>
</template>