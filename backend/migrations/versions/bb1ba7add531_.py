"""empty message

Revision ID: bb1ba7add531
Revises: 
Create Date: 2020-05-29 15:33:40.573274

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb1ba7add531'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amenity_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bed_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hash_password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('property_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('revoked_token_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('hash_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('accommodation',
    sa.Column('id', sa.String(length=32), nullable=False),
    sa.Column('member_id', sa.String(length=32), nullable=False),
    sa.Column('property_type_id', sa.Integer(), nullable=False),
    sa.Column('room_type_id', sa.Integer(), nullable=False),
    sa.Column('bed_type_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('special_notices', sa.Text(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('max_guess', sa.Integer(), nullable=False),
    sa.Column('num_bathrooms', sa.SmallInteger(), nullable=True),
    sa.Column('num_bedrooms', sa.SmallInteger(), nullable=True),
    sa.Column('num_beds', sa.SmallInteger(), nullable=True),
    sa.Column('apartment_manual', sa.Text(), nullable=True),
    sa.Column('apartment_rule', sa.Text(), nullable=True),
    sa.Column('direction_manual', sa.Text(), nullable=True),
    sa.Column('checkin_guide', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['bed_type_id'], ['bed_type.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['property_type_id'], ['property_type.id'], ),
    sa.ForeignKeyConstraint(['room_type_id'], ['room_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('amenity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amenity_category_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['amenity_category_id'], ['amenity_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('member_profile',
    sa.Column('member_id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('identify_documentID', sa.String(length=255), nullable=True),
    sa.Column('identify_document_url', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('member_id')
    )
    op.create_table('user_profile',
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.String(length=255), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.Column('avatar_url', sa.String(length=255), nullable=True),
    sa.Column('address', sa.String(length=255), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=32), nullable=True),
    sa.Column('member_id', sa.String(length=32), nullable=True),
    sa.Column('accommodation_id', sa.String(length=32), nullable=True),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('number_of_guess', sa.Integer(), nullable=False),
    sa.Column('number_of_night', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('check_in', sa.DateTime(), nullable=False),
    sa.Column('check_out', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('accommodation_id', sa.String(length=32), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accommodation_id', sa.String(length=32), nullable=True),
    sa.Column('member_id', sa.String(length=32), nullable=True),
    sa.Column('image_url', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('like',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=32), nullable=False),
    sa.Column('accommodation_id', sa.String(length=32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('link',
    sa.Column('accommodation_id', sa.String(length=32), nullable=False),
    sa.Column('amenity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['amenity_id'], ['amenity.id'], ),
    sa.PrimaryKeyConstraint('accommodation_id', 'amenity_id')
    )
    op.create_table('promotion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('accommodation_id', sa.String(length=32), nullable=True),
    sa.Column('member_id', sa.String(length=32), nullable=True),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('discount_amount', sa.Float(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['accommodation_id'], ['accommodation.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('promotion')
    op.drop_table('link')
    op.drop_table('like')
    op.drop_table('image')
    op.drop_table('comment')
    op.drop_table('booking')
    op.drop_table('user_profile')
    op.drop_table('member_profile')
    op.drop_table('amenity')
    op.drop_table('accommodation')
    op.drop_table('user')
    op.drop_table('room_type')
    op.drop_table('revoked_token_model')
    op.drop_table('property_type')
    op.drop_table('member')
    op.drop_table('bed_type')
    op.drop_table('amenity_category')
    # ### end Alembic commands ###
