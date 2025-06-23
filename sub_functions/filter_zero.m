% Threshold for zero (numerical tolerance)
threshold = eps * 100;

% Logical index for non-zero z-components
nonzero_idx = abs(target_field_out.b(3,:)) >= threshold;

% Filter coordinates and all b components
target_field_out.coords = target_field_out.coords(:, nonzero_idx);
target_field_out.b = target_field_out.b(:, nonzero_idx);

save("C:\Users\Fhlin\Documents\GitHub\CoilGen\target_fields\filtered_target_filed_out.mat", 'target_field_out');
