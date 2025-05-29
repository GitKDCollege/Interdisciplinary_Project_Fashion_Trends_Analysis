import streamlit as st

st.title("Dashboards and Visualizations")

feature_options = ['Discount%','Selling_Price','Counts','Interactive']
feature = st.selectbox("Choose a Feature to view Visualizations",feature_options)

sub_feature_options={
    'Discount%':['Master Dashboard','Highest Average Discount% by Brand','Lowest Average Discount% by Brand','Average Discount% Across Attire','Average Discount% Across Cloth','Average Discount% Across Gender','Max Discount% by Brand','Min Discount% by Brand','Max Discount% by Attire','Max Discount% by Cloth','Max Discount% by Gender'],

    'Selling_Price':['Master Dashboard','Highest Average Selling Price by Brand','Lowest Average Selling Price by Brand','Average Selling-Price Across Attire','Highest Average Selling Price by Cloth','Lowest Average Selling Price by Cloth','Average Selling-Price Across Gender','Average Selling Price by Brand and Attire','Average Selling Price by Brand and Cloth','Average Selling Price by Brand and Gender','Max Selling Price by Brand','Min Selling Price by Brand','Max Selling Price by Cloth','Min Selling Price by Cloth','Max Selling Price by Gender','Min Selling Price by Gender'],

    'Counts':['Master Dashboard','Top 10 Brands','Bottom 10 Brands','Total Count Across Attire','Highest Count Cloth','Lowest Count Cloth','Total Count Across Gender','Count of Attires Across Brand','Count of Cloth Across Brand','Count of Gender Across Brand'],

    'Interactive':['On Discount%','On Selling Price']
}

discount = {
    'Master Dashboard':"https://public.tableau.com/views/MyWork_17452062847250/DiscountsDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Highest Average Discount% by Brand':"https://public.tableau.com/views/MyWork_17452062847250/AvgDiscountbyBrand-Highest5?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Lowest Average Discount% by Brand':"https://public.tableau.com/views/MyWork_17452062847250/AvgDiscountbyBrand-Lowest5?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Average Discount% Across Attire':"https://public.tableau.com/views/MyWork_17452062847250/AvgDiscountbyAttire?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Average Discount% Across Cloth':"https://public.tableau.com/views/MyWork_17452062847250/AvgDiscountbyCloth?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Average Discount% Across Gender':"https://public.tableau.com/views/MyWork_17452062847250/AvgDiscountbyGender?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Max Discount% by Brand':"https://public.tableau.com/views/MyWork_17452062847250/MaxDiscountbyBrand-Highest5?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Min Discount% by Brand':"https://public.tableau.com/views/MyWork_17452062847250/MinDiscountbyBrand-Lowest5?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Max Discount% by Attire':"https://public.tableau.com/views/MyWork_17452062847250/MaxDiscountbyAttire?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Max Discount% by Cloth':"https://public.tableau.com/views/MyWork_17452062847250/MaxDiscountbyCloth?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Max Discount% by Gender':"https://public.tableau.com/views/MyWork_17452062847250/MaxDiscountbyGender?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
}

selling_price = {
    'Master Dashboard':"https://public.tableau.com/views/MyWork_17452062847250/SellingPriceDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Highest Average Selling Price by Brand':"https://public.tableau.com/views/MyWork_17452062847250/HighestAvgSellingPricebyBrand?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Lowest Average Selling Price by Brand':"https://public.tableau.com/views/MyWork_17452062847250/LowestAvgSellingPricebyBrand?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Average Selling-Price Across Attire':"https://public.tableau.com/views/MyWork_17452062847250/AvgSellingPricebyAttire?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Highest Average Selling Price by Cloth':"https://public.tableau.com/views/MyWork_17452062847250/HighestAvgSellingPricebyCloth?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Lowest Average Selling Price by Cloth':"https://public.tableau.com/views/MyWork_17452062847250/LowestAvgSellingPricebyCloth?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Average Selling-Price Across Gender':"https://public.tableau.com/views/MyWork_17452062847250/AvgSellingPricebyGender?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Average Selling Price by Brand and Attire':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsAttirevsAvgSellingPriceDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",
    
    'Average Selling Price by Brand and Cloth':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsClothvsAvgSellingPriceDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",
    
    'Average Selling Price by Brand and Gender':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsGendervsAvgSellingPriceDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Max Selling Price by Brand':"https://public.tableau.com/views/MyWork_17452062847250/MaxSellingPricebyBrand?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Min Selling Price by Brand':"https://public.tableau.com/views/MyWork_17452062847250/MinSellingPricebyBrand?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Max Selling Price by Attire':"https://public.tableau.com/views/MyWork_17452062847250/MaxSellingPricebyAttire?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",

    'Max Selling Price by Cloth':"https://public.tableau.com/views/MyWork_17452062847250/MaxSellingPricebyCloth?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Min Selling Price by Cloth':"https://public.tableau.com/views/MyWork_17452062847250/MinSellingPricebyCloth?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Max Selling Price by Gender':"https://public.tableau.com/views/MyWork_17452062847250/MaxSellingPricebyGender?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link",
    
    'Min Selling Price by Gender':"https://public.tableau.com/views/MyWork_17452062847250/MinSellingPricebyGender?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link"
}

counts = {
    'Master Dashboard':"https://public.tableau.com/views/MyWork_17452062847250/CountsDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Top 10 Brands':"https://public.tableau.com/views/MyWork_17452062847250/Top10Brands?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Bottom 10 Brands':"https://public.tableau.com/views/MyWork_17452062847250/Bottom10Brands?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Total Count Across Attire':"https://public.tableau.com/views/MyWork_17452062847250/CountbyAttire?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Highest Count Cloth':"https://public.tableau.com/views/MyWork_17452062847250/HighestSellingCloth?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Lowest Count Cloth':"https://public.tableau.com/views/MyWork_17452062847250/LowestSellingCloth?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Total Count Across Gender':"https://public.tableau.com/views/MyWork_17452062847250/CountbyGender?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Count of Attires Across Brand':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsAttireDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Count of Cloth Across Brand':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsClothDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",

    'Count of Gender Across Brand':"https://public.tableau.com/views/MyWork_17452062847250/BrandvsGenderDashboard?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link"
}

interactive = {
    'On Discount%':"https://public.tableau.com/views/MyWork_17452062847250/UltimateDashboard-Discount?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link",
    
    'On Selling Price':"https://public.tableau.com/views/MyWork_17452062847250/UltimateDashboard-SellingPrice?:language=en-GB&publish=yes&:sid=&:display_count=n&:origin=viz_share_link"
}

urls_dictionary = {
    'Discount%':discount,
    'Selling_Price':selling_price,
    'Counts':counts,
    'Interactive':interactive
}

sub_feature = st.selectbox("Choose the Visualization to View",sub_feature_options.get(feature))
urls = urls_dictionary.get(feature)
tableau_url = urls.get(sub_feature)

if "Master" in sub_feature:
    with open(f'./md_files/master_{feature}.md','r') as f:
        md_to_display = f.read()
else:
    md_to_display = ""


# HTML code for embedding Tableau using the JavaScript API
#X-Frame-Options, which is a security feature used by websites (including Tableau) to prevent their content from being embedded in iframes on other websites. Specifically, Tableau's settings on their server prevent your Streamlit app from displaying their dashboard directly using an iframe.

# Solution:
# Unfortunately, you cannot embed Tableau Public dashboards directly in an iframe within your Streamlit app due to this security restriction. However, there are a few alternatives you can try:

# Use Tableau’s Embedding API: Instead of using the iframe component, you can use the Tableau JavaScript API, which allows more control over embedding and could bypass some of the iframe restrictions. You'd need to use the JavaScript API in Streamlit's components.html()

def return_viz_html(viz_url):
    embed_code = f"""
    <html>
    <head>
        <script type="text/javascript" src="https://public.tableau.com/javascripts/api/tableau-2.min.js"></script>
        
    </head>
    <body>
        <div id="tableauViz" style="width: 100vw; height: 100vh;"></div>

        <script type="text/javascript">
            var viz;
            var containerDiv = document.getElementById('tableauViz');
            var url = "{viz_url}";

            var options = {{
                hideTabs: true,  // Allow tab navigation
                onFirstInteractive: function () {{
                    console.log("Tableau visualization is ready.");
                }}
            }};

            viz = new tableau.Viz(containerDiv, url, options);
        </script>
    </body>
    </html>
    """
    return embed_code

# Embed the HTML into Streamlit using components
st.markdown(md_to_display)
st.components.v1.html(return_viz_html(tableau_url), height=700, width=None)