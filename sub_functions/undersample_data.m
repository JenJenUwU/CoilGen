% Load the .mat file
data = load('C:\Users\Fhlin\Documents\GitHub\CoilGen\target_fields\target_field_out_scaled.mat');

% Extract the struct
tf = data.target_field_out;

% Undersample by taking every 4th column
tf.coords = tf.coords(:, 1:24:end);
tf.target_field_group_inds = tf.target_field_group_inds(:, 1:24:end);
tf.b = tf.b(:, 1:24:end);
tf.weights = tf.weights(:, 1:24:end);

% Save the undersampled struct
save('undersampled_target_field_1_24.mat', 'tf');
