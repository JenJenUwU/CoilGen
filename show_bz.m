close all;

%load data

%create an index to show only non-zero bz values;
ind=ones(size(target_field_out.coords(3,:)));
ind(find(abs(target_field_out.b(3,:))<eps*100))=nan;

%show 3d distribution
scatter3(target_field_out.coords(1,:),target_field_out.coords(2,:),target_field_out.coords(3,:),20,target_field_out.b(3,:).*ind,'filled');
axis vis3d
