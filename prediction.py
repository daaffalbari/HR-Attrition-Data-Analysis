import pandas as pd
import joblib

# Fungsi untuk memuat model dan encoder lalu melakukan prediksi pada input baru
def predict_attrition(input_data):
    """
    Melakukan prediksi apakah karyawan akan mengalami attrition atau tidak.
    
    Parameter:
    input_data (dict): Data input dalam bentuk dictionary dengan key yang sesuai dengan kolom input.
    
    Returns:
    str: Hasil prediksi (Attrition atau Tidak Attrition).
    """
    try:
        # Muat model dan encoder yang telah disimpan
        model = joblib.load('modelling.pkl')
        encoder = joblib.load('encoder.pkl')
        
        # Kolom kategorikal yang harus di-encode
        categorical_columns = ['BusinessTravel', 'Department', 'EducationField', 'JobRole', 'OverTime', 'MaritalStatus']
        
        # Buat DataFrame dari input data
        input_df = pd.DataFrame([input_data])
        
        # Encode kolom kategorikal pada data input
        encoded_input = encoder.transform(input_df[categorical_columns])
        encoded_input_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(categorical_columns))
        
        # Gabungkan data input yang sudah di-encode dengan kolom numerik lainnya
        input_df_reset = input_df.reset_index(drop=True)
        encoded_input_reset = encoded_input_df.reset_index(drop=True)
        final_input_df = pd.concat([input_df_reset.drop(categorical_columns, axis=1), encoded_input_reset], axis=1)
        
        # Lakukan prediksi
        prediction = model.predict(final_input_df)
        return "Attrition" if prediction[0] == 1 else "Tidak Attrition"
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

# Contoh penggunaan fungsi prediksi
if __name__ == "__main__":
    sample_input = {
        'BusinessTravel': 'Travel_Rarely',
        'Department': 'Sales',
        'EducationField': 'Life Sciences',
        'JobRole': 'Sales Executive',
        'OverTime': 'Yes',
        'MaritalStatus': 'Single',
    }
    result = predict_attrition(sample_input)
    print("Hasil prediksi:", result)