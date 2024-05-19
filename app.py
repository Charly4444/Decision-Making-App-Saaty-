from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from geteigs import geteigs  # Importing geteigs function to calculate eigenmax

app = Flask(__name__ , static_url_path='/static', static_folder='static')
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all routes

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/process_data', methods=['POST'])
def process_data():

    # Receive JSON data from the front end
    data = request.get_json()

    # Extract pairwise matrix and attribute matrices from the request
    pwmatrix = data.get('pwmatrix')
    attrmatrices = data.get('attrmatrices')
    
    try:
        # Calculate weights for the pairwise matrix
        weightofattr, eigvalm = geteigs(pwmatrix)
        # # convert to list
        weightofattr = list(weightofattr)
        # print("weightatr:",weightofattr)

        # Calculate weights for each attribute matrix
        listofweightofattrbychoices = []
        for attr_matrix in attrmatrices:
            wt, eigvalm = geteigs(attr_matrix)
            print("weight_atrr_choic:",wt)
            listofweightofattrbychoices.append(list(wt))
   
        
        # Calculate the final decision vector
        decisionvec = []
        for i in range(len(listofweightofattrbychoices[0])):
            summy = 0
            for j in range(len(listofweightofattrbychoices)):
                summy += listofweightofattrbychoices[j][i] * weightofattr[i]
            decisionvec.append(summy)


        print("decisionvec",decisionvec)
        # Return the computed results
        response_data = {
            'weightofattr': weightofattr,
            'listofweightofattrbychoices': listofweightofattrbychoices,
            'decisionvec': decisionvec
        }

        return jsonify(response_data)

    except Exception as e:
        # Handle errors gracefully
        error_message = f"Error occurred: {str(e)}"
        return jsonify({'error': error_message}), 500  # Return HTTP status code 500 for internal server error

if __name__ == '__main__':
    app.run(debug=True)
