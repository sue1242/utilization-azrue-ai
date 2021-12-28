def show_faces(image_path, detected_faces, show_id=False):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    try:
        #exif情報取得
        exifinfo = img._getexif()
        #exif情報からOrientationの取得
        orientation = exifinfo.get(0x112, 1)
        #画像を回転
        img = rotateImage(img, orientation)
        #回転した画像を保存（元の画像に上書き）
        img.save(image_path)
    except:
        #exif情報が取得できなかった場合は、そのまま処理を続ける
        #ホントは拡張子でexifを取得する、しないを判別した方がいいかもしれない。
        pass

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            if show_id:
                plt.annotate(face.face_id,(r.left, r.top + r.height + 15), backgroundcolor='white')
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

def show_face_attributes(image_path, detected_faces):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(detected_faces)
        prediction = ' (' + str(num_faces) + ' faces detected)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)

            # Annotate with face attributes (only age and emotion are used in this sample)
            detected_attributes = face.face_attributes.as_dict()
            age = 'age unknown' if 'age' not in detected_attributes.keys() else int(detected_attributes['age'])
            annotations = 'Person aged approximately {}'.format(age)
            txt_lines = 1
            if 'emotion' in detected_attributes.keys():
                for emotion_name in detected_attributes['emotion']:
                    txt_lines += 1
                    annotations += '\n - {}: {}'.format(emotion_name, detected_attributes['emotion'][emotion_name])
            plt.annotate(annotations,((r.left + r.width), (r.top + r.height + (txt_lines * 12))), backgroundcolor='white')

        # Plot the image
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(prediction)

    plt.axis('off')
    plt.imshow(img)

def show_similar_faces(image_1_path, image_1_face, image_2_path, image_2_faces, similar_faces):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Create a figure to display the results
    fig = plt.figure(figsize=(16, 6))

    # Show face 1
    img1 = Image.open(image_1_path)
    r = image_1_face.face_rectangle
    bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
    draw = ImageDraw.Draw(img1)
    draw.rectangle(bounding_box, outline='magenta', width=5)
    a = fig.add_subplot(1,2,1)
    plt.axis('off')
    plt.imshow(img1)

    # get the matching face IDs
    matching_face_ids = list(map(lambda face: face.face_id, similar_faces))

    # Draw a rectangle around each similar face in image 2
    img2 = Image.open(image_2_path)
    a = fig.add_subplot(1,2,2)
    plt.axis('off')
    for face in image_2_faces:
        r = face.face_rectangle
        bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
        draw = ImageDraw.Draw(img2)
        if face.face_id in matching_face_ids:
            draw.rectangle(bounding_box, outline='lightgreen', width=10)
            plt.annotate('Match!',(r.left, r.top + r.height + 15), backgroundcolor='white')
        else:
            draw.rectangle(bounding_box, outline='red', width=5)
    plt.imshow(img2)
    plt.show()

def show_recognized_faces(image_path, detected_faces, recognized_face_names):
    import matplotlib.pyplot as plt
    from PIL import Image, ImageDraw

    # Open an image
    img = Image.open(image_path)

    # Create a figure to display the results
    fig = plt.figure(figsize=(8, 6))

    if detected_faces:
        # If there are faces, how many?
        num_faces = len(recognized_face_names)
        caption = ' (' + str(num_faces) + ' faces recognized)'
        # Draw a rectangle around each detected face
        for face in detected_faces:
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(img)
            draw.rectangle(bounding_box, outline='magenta', width=5)
            if face.face_id in recognized_face_names:
                plt.annotate(recognized_face_names[face.face_id],
                             (r.left, r.top + r.height + 15), backgroundcolor='white')
        #a = fig.add_subplot(1,1,1)
        fig.suptitle(caption)

    plt.axis('off')
    plt.imshow(img)

def rotateImage(img, orientation):
    """
    画像ファイルをOrientationの値に応じて回転させる
    """
    #orientationの値に応じて画像を回転させる
    if orientation == 1:
        pass
    elif orientation == 2:
        #左右反転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif orientation == 3:
        #180度回転
        img_rotate = img.transpose(Image.ROTATE_180)
    elif orientation == 4:
        #上下反転
        img_rotate = img.transpose(Image.FLIP_TOP_BOTTOM)
    elif orientation == 5:
        #左右反転して90度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
    elif orientation == 6:
        #270度回転
        img_rotate = img.transpose(Image.ROTATE_270)
    elif orientation == 7:
        #左右反転して270度回転
        img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
    elif orientation == 8:
        #90度回転
        img_rotate = img.transpose(Image.ROTATE_90)
    else:
        pass

    return img_rotate