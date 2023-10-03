import pandas as pd
import matplotlib.pyplot as plt

# 1- Load the CSV dataset
dataset = pd.read_csv('diabetes.csv')


# 2- Data cleaning
dataset = dataset.drop_duplicates()  # Remove duplicate rows
dataset = dataset.dropna()  # Drop rows with missing values

# 3- know information about columns
print(dataset.info())

# 4- know values of Dataset
print(dataset)


# 5-"Export the cleaned dataset to Excel" to show Dataset obvisouly
dataset.to_excel('clean_diabetes.xlsx', index=False)


# 6-Make New Columns in Dataset depend on the Dataset Columns -> "Visulazations"
# By Making of functions to make values of new column in Dataset depend on Dataset Columns

# Define a function to determine the Pregnancies type  based on the 'Pregnancies' value
def get_pregnancies_type(pregnancies):
    if 0 <= pregnancies <= 5:
        return '0 to 5'
    elif 6 <= pregnancies <= 10:
        return '6 to 10'
    else:
        return 'higher than 10'

#  6-1 Create the 'Pregnancies_type' column using the 'Pregnancies' column as input
dataset['Pregnancies_type'] = dataset['Pregnancies'].apply(get_pregnancies_type)


# Define a function to determine the Glucose type  based on the 'Glucose' value
def get_Glucose_type(glucose):
    if 0 <= glucose <=99:
        return 'Normal'
    elif 100 <= glucose<=125:
        return 'Prediabetes'
    else:
        return 'Diabetes'

# 6-2 Create the 'Glucose_type' column using the 'Glucose' column as input
dataset['Glucose_type'] = dataset['Glucose'].apply(get_Glucose_type)

# Define a function to determine the Blood Pressure type  based on the 'Blood Pressure' value
def get_Blood_Pressure_type(blood_pressure):
    if 40 <= blood_pressure <= 60:
        return 'Low'
    elif 61 <= blood_pressure <=80:
        return 'Normal'
    elif 81 <= blood_pressure <=200:
        return 'High'
    else:
        return 'Abnormal'

# 6-3 Create the 'Blood_Pressure_type' column using the 'Blood_Pressure' column as input
dataset['Blood_Pressure_type'] = dataset['BloodPressure'].apply(get_Blood_Pressure_type)

# Define a function to determine the skin thickness type  based on the 'skin thickness' value
def get_skin_thickness_type(skin_thickness):
    if 0 <= skin_thickness <= 10:
        return 'very thin'
    elif 11 <= skin_thickness <= 20:
        return 'Thin'
    elif 21 <= skin_thickness <=30:
        return 'medium'
    elif 31 <= skin_thickness <= 40:
        return 'Thick'
    else:
        return 'Very Thick'

# 6-4 Create the 'skin_thickness_type' column using the 'skin_thickness' column as input
dataset['SkinThickness_type'] = dataset['SkinThickness'].apply(get_skin_thickness_type)

# Define a function to determine the Insulin type  based on the 'insulin' value
def get_Insulin_type(insulin):
    if 0 <= insulin <= 50:
        return 'Low'
    elif 51 <= insulin <=100:
        return 'Medium'
    else:
        return 'High'

# 6-5 Create the 'Insulin_type' column using the 'Insulin' column as input
dataset['Insulin_type'] = dataset['Insulin'].apply(get_Insulin_type)

# Define a function to determine the bmi type  based on the 'BMI' value
def get_BMI_type(bmi):
    if 0 <= bmi <= 18.5:
        return 'Under Weight'
    elif 18.6 <= bmi <= 24.9:
        return 'Optimum Range'
    elif 25 <= bmi <=29.9:
        return 'Overweight'
    elif 30 <= bmi <= 34.9:
        return 'Class I obesity'
    elif 35 <= bmi <= 39.9:
        return 'Class II obesity'
    else:
        return 'Class III obesity'

# 6-6 Create the 'BMI_type' column using the 'BMI' column as input
dataset['BMI_type'] = dataset['BMI'].apply(get_BMI_type)


# Define a function to determine the DiabetesPedigreeFunction type  based on the 'DiabetesPedigreeFunction' value
def get_DiabetesPedigreeFunction_type(DiabetesPedigreeFunction):
    if 0 <= DiabetesPedigreeFunction <=0.499:
        return '0 to 0.5'
    elif 0.501<= DiabetesPedigreeFunction<=0.997 :
        return '0.6 to 1'
    elif 1.001<= DiabetesPedigreeFunction<=1.476 :
        return '1.1 to 1.5'
    else:
        return 'higher than 1.5'

# 6-7 Create the 'DiabetesPedigreeFunction_type' column using the 'DiabetesPedigreeFunction' column as input
dataset['DiabetesPedigreeFunction_type'] = dataset['DiabetesPedigreeFunction'].apply(get_DiabetesPedigreeFunction_type)


# Define a function to determine the age range based on the 'age' value
def get_age_range(age):
    if 20 <= age <= 30:
        return '20 to 30'
    elif 31 <= age <= 40:
        return '31 to 40'
    elif 41 <= age <= 50:
        return '41 to 50'
    elif 51 <= age <= 60:
        return '51 to 60'
    else:
        return 'higher than 61'

# 6-8 Create the 'age_range' column using the 'age' column as input
dataset['age_range'] = dataset['Age'].apply(get_age_range)

# Define a function to determine the outcome  based on the 'outcome' value
def get_outcome(outcome):
    if outcome==0:
        return 'non-diabetes'
    elif outcome ==1 :
        return 'diabetes'

# 6-9 Create the 'outcome_type' column using the 'outcome' column as input
dataset['outcome_type'] = dataset['Outcome'].apply(get_outcome)

# 7 "Export the modifiyed dataset to Excel"
dataset.to_excel('Modified_diabetes.xlsx', index=False)


# 8 visualizations

# 8-1 Diabetes and non-Diabetes by Pregnancies
# Count the occurrences of each combination of 'Pregnancies_type' and 'outcome_type'
grouped_data = dataset.groupby(['Pregnancies_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by Pregnancies')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('Pregnancies_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-2 Diabetes and non-Diabetes by Glucose

# Count the occurrences of each combination of 'Glucose_type' and 'outcome_type'
grouped_data = dataset.groupby(['Glucose_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by Glucose')

# remove legend
ax.get_legend().remove()

# Save the chart as an image file (e.g., PNG format)
plt.savefig('Glucose_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-3 Diabetes and non-Diabetes by Blood Pressure

# Count the occurrences of each combination of 'Glucose_type' and 'outcome_type'
grouped_data = dataset.groupby(['Blood_Pressure_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by Blood Pressure')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('Blood_Pressure_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-4 Diabetes and non-Diabetes by SkinThickness

# Count the occurrences of each combination of 'SkinThickness_type' and 'outcome_type'
grouped_data = dataset.groupby(['SkinThickness_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by SkinThickness')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('SkinThickness_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-5 Diabetes and non-Diabetes by Insulin

# Count the occurrences of each combination of 'Insulin_type' and 'outcome_type'
grouped_data = dataset.groupby(['Insulin_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by Insulin')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('Insulin_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()


# 8-6 Diabetes and non-Diabetes by BMI

# Count the occurrences of each combination of 'MBI_type' and 'outcome_type'
grouped_data = dataset.groupby(['BMI_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by BMI')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('BMI_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-7 Diabetes and non-Diabetes by DiabetesPedigreeFunction

# Count the occurrences of each combination of 'DiabetesPedigreeFunction_type' and 'outcome_type'
grouped_data = dataset.groupby(['DiabetesPedigreeFunction_type', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by DiabetesPedigreeFunction')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('DiabetesPedigreeFunction_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

# 8-8 Diabetes and non-Diabetes by Age

# Count the occurrences of each combination of 'Age_type' and 'outcome_type'
grouped_data = dataset.groupby(['age_range', 'outcome_type']).size().unstack(fill_value=0)

# Sort the columns by their sum (smallest to largest)
grouped_data = grouped_data.loc[:, grouped_data.sum().sort_values().index]

# Define the colors for the columns
column_colors = ['darkorange', 'blue']  # Change this to the desired colors

# Create the horizontal bar chart with the specified column colors
ax = grouped_data.plot(kind='barh', stacked=False, color=column_colors)

# Add labels next to each bar
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2.), ha='left', va='center', xytext=(5, 0), textcoords='offset points')

# Remove the x-axis
ax.xaxis.set_visible(False)

# Remove frame around the chart
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Set the y-axis label
plt.ylabel('')

# Set the title
plt.title('Diabetes and non-Diabetes by Age')

# Add the legend
plt.legend(title='Outcome')

# Save the chart as an image file (e.g., PNG format)
plt.savefig('Age_bar_chart.png', bbox_inches='tight', dpi=300)

# Display the chart
plt.show()

