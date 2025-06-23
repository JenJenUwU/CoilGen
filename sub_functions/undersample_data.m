% Load the .mat file
data = load('C:\Users\Fhlin\Documents\GitHub\CoilGen\target_fields\test.mat');

% Extract the struct
target_field_out = data.target_field_out;

% Undersample by taking every 4th column
target_field_out.coords = target_field_out.coords(:, 1:4:end);
target_field_out.target_field_group_inds = target_field_out.target_field_group_inds(:, 1:4:end);
target_field_out.b = target_field_out.b(:, 1:4:end);
target_field_out.weights = target_field_out.weights(:, 1:4:end);

% Save the undersampled struct
save('C:\Users\Fhlin\Documents\GitHub\CoilGen\target_fields\new_test.mat', 'target_field_out');
